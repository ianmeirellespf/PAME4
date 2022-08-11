from app.user.model import User , verify_password
from app.user.schemas import Userschema ,UserLoginschema
from app.user.services import user_services
from flask import request, jsonify, render_template
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from app.utils.filters import filter


class UserPost(MethodView): 

    def post(self):
        schema = Userschema()
        user = user_services.create(request.json, schema=schema)

        return schema.dump(user)

class UserId(MethodView): 
	
    decorators = [jwt_required()]
    def get(self, id):
        schema = filter.getSchema(
                                  qs = request.args, schema_cls = Userschema
                                   )

        user = user_services.get_by_id(id)

        return schema.dump(user), 200

    
    def put(self, id):

    
        schema = Userschema()
        user = user_services.update_by_id(id, request.json, schema=schema)

        return schema.dump(user), 200

    
    def patch(self, id):

        schema = Userschema()
        user = user_services.update_by_id(id, request.json, schema=schema, partial=True)

        return schema.dump(user), 200

    
    def delete(self, id):

        user_services.delete_by_id(id)


class UserLogin(MethodView): 

    def post(self):

        schema = UserLoginschema()
        dados = schema.load(request.json)

        user = user_services.get_by_email(dados['email'])

        if not user or not user.verify_password(dados['senha']):
            return {"error": "usuario ou senha invalidos"}
        
        token = create_access_token(identity=user.id)
        
        return {"user": Userschema().dump(user),
                "token": token}, 200
