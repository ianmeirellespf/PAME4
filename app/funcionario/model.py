from app.extensions import db
from app.model import BaseModel




class Funcionario(BaseModel):

    __tablename__ = "funcionario"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    cpf=db.Column(db.String(11), unique = True, nullable = False)
    email = db.Column(db.String(100) , nullable = False)
    senha = db.Column(db.String(100) , nullable = False)
    idade=db.Column(db.Integer)
    salario =db.Column(db.Float)
    endereço = db.Column(db.String(100))
    telefone = db.Column(db.String(16))
    cargo =db.Column(db.String(30))
    genero=db.Column(db.String(16))
    #relacionamentos
    unidadetrab = db.Column(db.Integer, db.ForeignKey("unidade.id"))

    def json(self):

        return{
            
            "nome": self.nome ,
            "cpf": self.cpf , #o CPF assim como em alguns sites, será o "username" de login.
            "email": self.email ,
            "endereço": self.endereço ,
            "idade": self.idade ,
            "salario": self.salario ,
            "telefone": self.telefone ,
            "cargo": self.cargo ,
            "genero": self.genero 
            
        }
    