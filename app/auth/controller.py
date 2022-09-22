from app.user.schemas import Userschema ,UserLoginschema
from app.user.services import user_services
from app.user.model import User
from app.auth.schemas import SenhaNovaSchema
from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required , get_jwt_identity , create_access_token
from datetime import timedelta
import string
import random
from flask_mail import Message
from flask import request, render_template
from app.extensions import mail

class Login(MethodView): 

    def post(self):

        schema = UserLoginschema()
        dados = schema.load(request.json)

        user = user_services.get_by_email(dados['email'])

        if not user or not user.verify_password(dados['senha']):
            return {"error": "usuario ou senha invalidos"}
        
        token = user.token()

        refresh_token = user.refresh_token()
        

        return {"user": Userschema().dump(user),
                "token": token,
                "refresh_token": refresh_token}, 200

class TokenRefresh(MethodView):

    decorators = [jwt_required(refresh = True)]

    def get(self) :

        user_id = get_jwt_identity()
        user = user_services.get_by_id(user_id)

        token = create_access_token(identity=user_id,
           expires_delta=timedelta(minutes=1000),
           fresh=False,
           additional_claims = {"role" : user.role})

        refresh_token = user.refresh_token()

        return {"user": Userschema().dump(user),
                "token": token,
                "refresh_token": refresh_token
                } , 200


class MudaSenhaEmail(MethodView): # /esquecisenhaemail

    def post(self):
        schema = UserLoginschema()
        
        dados = schema.load(request.json)
        user = User.query.filter_by(email=dados['email']).first_or_404()
        
        tamanho_string = 50
        
        PinVerificação = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(tamanho_string))
        
        user.PinVerificação = PinVerificação
        user.save()

        #mandando email de mudança de senha com pin.
        msg = Message(sender= 'ianmeirelles@poli.ufrj.br',
             recipients=[user.email],subject='mudança de senha',
             html= render_template('mudaSenha.html', nome = user.nome))
            
        mail.send(msg)

        return user.json(), 200

        

class NovaSenhaFeita(MethodView): # /NovaSenhaFeita

    def patch(self):
        dados = SenhaNovaSchema()
        
        dados = dados.load(request.json)
        

        user = User.query.filter_by(email=dados['email']).first_or_404()

        if  not user.verificar_pin(dados['PinVerificação']):
            return {"erro": "pin incorreto"}, 401

        
        user.senha = dados['senha']
        user.save()

        return {"msg": "senha nova salva"},  200