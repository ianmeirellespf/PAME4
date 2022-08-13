from app.user.schemas import Userschema ,UserLoginschema
from app.user.services import user_services
from flask import request
from flask.views import MethodView




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
