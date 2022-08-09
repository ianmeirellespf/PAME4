from ..extensions import ma
from ..user.model import User

class Userschema(ma.SQLAlchemySchema) :

   class Meta :
    model= User
    load_instance = True
    ordered = True

    id = ma.Integer(dump_only=True)
    nome = ma.String(requiered = True)
    email =ma.Email(requiered = True)
    cpf=ma.String(requiered = True)
    senha=ma.String(load_only=True ,requiered = True)
    data_nascimento = ma.String(requiered = True)
    genero = ma.String(requiered = True)

