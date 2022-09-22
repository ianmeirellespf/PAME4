from ..extensions import ma
from ..user.model import User
from marshmallow import fields

class Userschema(ma.SQLAlchemySchema) :

    class Meta:
        model= User
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    nome = ma.String(required = True)
    email =ma.Email(required = True)
    cpf=ma.String(required = True)
    senha=ma.String(load_only=True ,required = True)
    data_nascimento = ma.String(required = True)
    genero = ma.String(required = True)
    role = ma.String()

class UserLoginschema(ma.Schema):
    email = ma.Email(required=True)
    senha = ma.String(required=True, load_only=True)

class UserEmailschema(ma.Schema):
    email = ma.Email(required=True)
    


