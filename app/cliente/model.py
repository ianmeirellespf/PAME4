from app.extensions import db
from app.model import BaseModel



class clienteUnidade(BaseModel):
    __tablename__ = "cliente_unidade"

    id = db.Column(db.Integer , primary_key=True)

    cliente = db.Column(db.Integer , db.ForeignKey("cliente.id"))
    unidade = db.Column(db.Integer , db.ForeignKey("unidade.id"))

class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    cpf=db.Column(db.String(11), unique = True, nullable = False)
    email = db.Column(db.String(100), nullable = False)
    senha = db.Column(db.String(100) , nullable = False)
    endereço = db.Column(db.String(100)) # a principio pode ficar como nulo, mas quando for desenvolvido o app, vai ajudar .
    idade=db.Column(db.Integer)
    genero=db.Column(db.String(16))
    #relacionamentos
    unidades = db.relationship("Unidade", secondary = "cliente_unidade", backref="cliente")
    compras = db.relationship("Venda", backref="cliente")
    
    def json(self):

        return{
            
            "nome": self.nome ,
            "cpf": self.cpf ,  #o CPF assim como em alguns sites, será o "username" de login.
            "email": self.email ,
            "endereço": self.endereço ,
            "idade": self.idade ,
            "genero": self.genero 
            
        }


    