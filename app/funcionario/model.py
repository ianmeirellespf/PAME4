from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

funcionario_api = Blueprint("funcionario_api", __name__)



class Funcionario(BaseModel):

    __tablename__ = "funcionario"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    cpf=db.Column(db.String(11))
    email = db.Column(db.String(100))
    idade=db.Column(db.Integer)
    genero=db.Column(db.String(16))
    salario =db.Column(db.Float)
    endereço = db.Column(db.String(100))
    telefone = db.Column(db.String(16))
    cargo =db.Column(db.String(30))
    unidade = db.Column(db.Integer, db.ForeignKey("unidade.id"))
    