from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

class clienteUnidade(BaseModel):
    __tablename__ = "cliente_unidade"

    id = db.Column(db.Integer , primary_key=True)

    cliente = db.Column(db.Integer , db.ForeignKey("cliente.id"))
    unidade = db.Column(db.Integer , db.ForeignKey("unidade.id"))

class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    cpf=db.Column(db.String(11) , unique = True)
    email = db.Column(db.String(100))
    endereço = db.Column(db.String(100)) # a principio pode ficar como nulo, mas quando for desenvolvido o app, vai ajudar .
    idade=db.Column(db.Integer)
    genero=db.Column(db.String(16))
    #relacionamentos
    unidades = db.relationship("unidade", secondary = "cliente_unidade", backref="clientes")
    compras = db.relationship("Venda", backref="cliente")
    
    def json(self):

        return{
            "id": self.id ,
            "nome": self.nome ,
            "cpf": self.cpf ,
            "email": self.email ,
            "endereço": self.endereço ,
            "idade": self.idade ,
            "genero": self.genero ,
            "unidades": self.unidades ,
            "compras": self.compras 
        }


    