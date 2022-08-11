from app.extensions import db
from app.model import BaseModel
import bcrypt

class User(BaseModel):

    __tablename__ = "user"

    nome = db.Column(db.String(100))
    email =db.Column(db.String(100) , unique = True)
    cpf=db.Column(db.String(11) , unique = True) #nesse caso , a receita é em relação ao dinheiro
    senha_hash=db.Column(db.LargeBinary(128) )
    data_nascimento = db.Column(db.String(20))
    genero = db.Column(db.String(20))


    #relacionamento many-to-many
    #salas()

@property
def senha(self):
    "retorna que a senha não pode ser mostrada"
    raise AttributeError('A senha não é um atributo chamavel')
   
@senha.setter
def  senha(self,senha) -> None:

    '''função que vai codificar a senha''' 
    self.senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) 


def verify_password (self, senha) -> bool  :
    '''função que compara a senha'''

    return bcrypt.checkpw(senha.encode(),self.senha_hash) 