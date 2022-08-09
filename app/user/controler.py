
from app.user.model import User
from flask import request , jsonify , render_template
from flask.views import MethodView
from flask_mail  import Message
from flask_jwt_extended import creat_acess_token , jwt_required
from app.extensions import mail , jwt
import bcrypt
from ..user.schemas import Userschema
from ..user.services import user_services

class UserCreate(MethodView):  

    def post(self):

        schema = Userschema()
        user = user_services.create(request.json , schema)

        mensagem = Message( sender =  "ianmeirelles@poli.ufrj.br",
                            recipients= [user.email],
                            subject= "Bem vindo ao ClassShare",
                            html =render_template('email.html', nome = user.nome) )

        mail.send(mensagem)

        return schema.dump( user ) , 201
