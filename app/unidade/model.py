from app.extensions import db
from app.model import BaseModel


class Unidade(BaseModel):

    __tablename__ = "unidade"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    endereço=db.Column(db.String(100) , unique = True)
    receita=db.Column(db.Float) #nesse caso , a receita é em relação ao dinheiro
    lucro=db.Column(db.Float)
    horaAbre=db.Column(db.String(16))#o horario ja virá tratado pelo fronte trate
    horaFecha=db.Column(db.String(16))#o horario ja virá tratado pelo fronte trate
    #relacionamentos
    funcionarios= db.relationship("Funcionario", backref="unidade")

    def json(self):

        return{
            
            "nome": self.nome ,
            "endereço": self.endereço ,
            "receita": self.receita ,
            "lucro": self.lucro ,
            "horaAbre": self.horaAbre ,
            "horaFecha": self.horaFecha      
        }
    
    