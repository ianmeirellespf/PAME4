from app.extensions import db
from app.model import BaseModel


class VendaProduto(BaseModel):
    __tablename__ = "venda_produto"

    id = db.Column(db.Integer , primary_key=True)

    venda = db.Column(db.Integer , db.ForeignKey("venda.id"))
    produto = db.Column(db.Integer , db.ForeignKey("produto.id"))

class Venda(BaseModel):

    __tablename__ = "venda"

    id = db.Column(db.Integer , primary_key=True)
    valor = db.Column(db.Float)
    data= db.Column(db.String(50)) #a data ja deveria vir tratada pelo front trate ,  pois o ifinstance não está aceitando.
    avaliaçao=db.Column(db.Float) #avaliação da qualidade do atendimento e todo o conjunto 
    delivery = db.Column(db.Boolean) #quando o app for desenvolvido , vai ajudar a saber se era ou não delivery, por ser atrelado a um cliente, o endereço ja estará la.
    #relacionamentos
    produtos = db.relationship("Produto", secondary = "venda_produto", backref="vendascontendo")
    clientecomprou = db.Column(db.Integer, db.ForeignKey("cliente.id"))


    def json(self):

        return{
            
            "valor": self.valor ,
            "data": self.data ,
            "avaliaçao": self.avaliaçao ,
            "delivery": self.delivery
         }
            

    
    