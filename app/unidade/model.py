from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

unidade_api = Blueprint("unidade_api", __name__)

class Unidade(BaseModel):

    __tablename__ = "unidade"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    endereço=db.Column(db.String(100))
    receita=db.Column(db.Float)
    lucro=db.Column(db.Float)
    horaAbre=db.Column(db.String(16))#o horario ja virá tratado pelo fronte trate
    horaFecha=db.Column(db.String(16))#o horario ja virá tratado pelo fronte trate
    funcionarios= db.relationship("funciorario", backref="unidade")
    
    