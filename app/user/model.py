from app.extensions import db
from app.model import BaseModel
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required , create_refresh_token , decode_token
from datetime import timedelta
from app.aluno.model import Aluno
from app.professor.model import Professor
from app.permissions import self_aluno_only , self_professor_only
from datetime import datetime

class User(BaseModel):

    __tablename__ ="user"

    nome = db.Column(db.String(100))
    email =db.Column(db.String(100) , unique = True)
    cpf=db.Column(db.String(11) , unique = True) #nesse caso , a receita é em relação ao dinheiro
    senha_hash=db.Column(db.LargeBinary(128))
    data_nascimento = db.Column(db.String(20))
    role_user = db.Column(db.String(30))
    genero = db.Column(db.String(20))
    PinVerificaçãoHash = db.Column(db.LargeBinary(128))


    #relacionamento one-to-many
    professor= db.relationship('Professor' , back_populates = 'user' , uselist = False)
    aluno= db.relationship('Aluno' , back_populates = 'user' , uselist = False)
    #salas()



    

    def role_specify(self):
        if self.role_user == 'aluno':
            user_specified = Aluno(user_id=self.id)
            user_specified.save()
        else:
            user_specified = Professor(user_id=self.id)
            user_specified.save()




    @property
    def role(self):

        '''Function that returns the role of the user'''

        return self.role_user


    @role.setter
    def role(self, role):

        '''Function that verifies if the role input 
        is correct and sets it. 
        
        Roles --> Admin, Provider'''

        if role.lower() in ('aluno','professor'):
            self.role_user = role

        else: 
            raise KeyError('User role not specified')
    @property
    def senha(self):
        "retorna que a senha não pode ser mostrada"
        raise AttributeError('A senha não é um atributo chamavel')
    
    @senha.setter
    def  senha(self,senha) -> None:

        '''função que vai codificar a senha''' 
        self.senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) 


    def verify_password (self, senha) -> bool  :
        '''função que compara a senha'''

        return bcrypt.checkpw(senha.encode(),self.senha_hash) 

    def token(self) -> str:
        return create_access_token(
            identity = self.id,
            additional_claims = {'role': self.role},
            expires_delta = timedelta(minutes=1440), 
            fresh=True
        )


    def refresh_token(self) -> str:
        
        return create_refresh_token(
            identity = self.id,
            additional_claims={'role': self.role},
            expires_delta = timedelta(minutes=2880)
        )


    @staticmethod
    def verify_token(token) -> object:
        try:
            data = decode_token(token)
        except:
            return None

        user = User.query.get(data['identity'])

        return user

    @property
    def PinVerificação(self):
        raise AttributeError('O Pin de verificação não é um atributo chamavel')
        
    @PinVerificação.setter
    def PinVerificação(self, PinVerificação):
        
         self.PinVerificaçãoHash = bcrypt.hashpw(PinVerificação.encode(), bcrypt.gensalt())
        
    def verificar_pin(self, verificaPin):
        
        return bcrypt.checkpw(verificaPin.encode(), self.PinVerificaçãoHash)