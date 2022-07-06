from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

produto_api = Blueprint("produto_api", __name__)



class Produto(BaseModel):

    __tablename__ = "produto"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(50))
    valor = db.Column(db.Float)
    estoque= db.Column(db.Integer)
    validade = db.Column(db.Date)
    localEstoque = db.Column(db.String(6))     # esse e o abaixo so indicam em que locais da loja ficará o produto, por organização.
    localBalcao = db.Column(db.String(6))
    categoria = db.Column(db.String(50))       # como beleza, higiene e etc.
    receita = db.Column(db.Boolean)            #o True indicaria a necessidade de receita.