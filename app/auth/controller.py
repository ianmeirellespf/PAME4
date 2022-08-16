from app.user.schemas import Userschema ,UserLoginschema
from app.user.services import user_services
from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required , get_jwt_identity , create_access_token
from datetime import timedelta



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
