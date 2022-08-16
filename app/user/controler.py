from app.user.model import *
from app.user.schemas import Userschema 
from app.user.services import user_services
from flask import request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required , create_refresh_token , get_jwt_identity
from app.utils.filters import filter
from app.permissions import self_aluno_only , self_professor_only


class UserPost(MethodView): 

    def post(self):
        schema = Userschema()
        user = user_services.create(request.json, schema=schema)
        user.role_specify()

        return schema.dump(user)

class UserId(MethodView): 
	
    decorators = [jwt_required(),self_aluno_only()]
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


