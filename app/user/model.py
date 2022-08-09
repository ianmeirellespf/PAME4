from app.extensions import db
from app.model import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    nome = db.Column(db.String(100))
    email =db.Column(db.String(100) , unique = True)
    cpf=db.Column(db.String(11) , unique = True) #nesse caso , a receita é em relação ao dinheiro
    senha=db.Column(db.String(100) , unique = True , nullable = False)
    data_nascimento = db.Column(db.String(20))
    genero = db.Column(db.String(20))


    #relacionamento many-to-many
    #salas()

   
    
    