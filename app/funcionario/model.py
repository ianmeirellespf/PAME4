from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

funcionario_api = Blueprint("funcionario_api", __name__)



class Funcionario(BaseModel):

    __tablename__ = "funcionario"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    cpf=db.Column(db.String(11), unique = True)
    email = db.Column(db.String(100))
    idade=db.Column(db.Integer)
    salario =db.Column(db.Float)
    endereço = db.Column(db.String(100))
    telefone = db.Column(db.String(16))
    cargo =db.Column(db.String(30))
    genero=db.Column(db.String(16))
    #relacionamentos
    unidade = db.Column(db.Integer, db.ForeignKey("unidade.id"))

    def json(self):

        return{
            "id": self.id ,
            "nome": self.nome ,
            "cpf": self.cpf ,
            "email": self.email ,
            "endereço": self.endereço ,
            "idade": self.idade ,
            "salario": self.salario ,
            "telefone": self.telefone ,
            "cargo": self.cargo ,
            "genero": self.genero ,
            "unidade": self.unidade 
            
        }
    