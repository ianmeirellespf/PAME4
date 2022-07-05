from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

venda_api = Blueprint("venda_api", __name__)

class VendaProduto(BaseModel):
    __tablename__ = "venda_produto"

    id = db.Column(db.Integer , primary_key=True)

    venda = db.Column(db.Integer , db.ForeignKey("venda.id"))
    produto = db.Column(db.Integer , db.ForeignKey("produto.id"))

class Venda(BaseModel):

    __tablename__ = "venda"

    id = db.Column(db.Integer , primary_key=True)
    valor = db.Column(db.Float)
    data= db.Column(db.Date)
    produtos = db.relationship("produto", secondary = "venda_produto", backref="vendascontendo")
    cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    avaliaçao=db.Column(db.Float)   #avaliação da qualidade do atendimento e todo o conjunto 