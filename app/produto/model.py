from app.extensions import db
from app.model import BaseModel




class Produto(BaseModel):

    __tablename__ = "produto"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(50))
    valor = db.Column(db.Float)
    estoque= db.Column(db.Integer)
    validade = db.Column(db.String(20))        #a data ja deveria vir tratada pelo front trate ,  pois o ifinstance não está aceitando.
    marca = db.Column(db.String(50))
    localEstoque = db.Column(db.String(6))     # esse e o abaixo so indicam em que locais da loja ficará o produto, por organização.
    localBalcao = db.Column(db.String(6))
    categoria = db.Column(db.String(50))       # como beleza, higiene e etc.
    receita = db.Column(db.Boolean)            #o True indicaria a necessidade de receita.
    lote = db.Column(db.String(50) , unique = True)

    def json(self):

        return{
            
            "nome": self.nome ,
            "valor": self.valor ,
            "estoque": self.estoque ,
            "validade": self.validade ,
            "marca": self.marca ,
            "localEstoque": self.localEstoque ,
            "localBalcao": self.localBalcao ,
            "categoria": self.categoria ,
            "receita": self.receita ,
            "lote": self.lote 
            
        }