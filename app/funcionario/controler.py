from app.funcionario.model import Funcionario
from flask import render_template,request , jsonify
from flask_jwt_extended import create_access_token
from flask.views import MethodView
from flask_mail import Message
from app.extensions import mail
import bcrypt


class funcionarioCreate(MethodView):  # a rota dela é /registrofun

    def post(self):

        body = request.json

        #id = body.get('id') #nao é necessario ,  no final do codigo seria tirado.
        nome = body.get('nome')
        cpf=body.get('cpf')
        email = body.get('email')
        senha = body.get('senha')
        senha = bcrypt.hashpw(senha.encode() , bcrypt.gensalt()).decode() #tornando a senha em criptografia  e adicionando o salt, para não atrapalhar senhas iguais em caso de hacker.
        endereço = body.get('endereço') 
        idade=body.get('idade')
        salario=body.get('salario')
        telefone=body.get('telefone')
        cargo=body.get('cargo')
        genero=body.get('genero')
        

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(senha,str) and \
                            isinstance(endereço,str) and \
                                isinstance(idade,int) and \
                                    isinstance(salario,float) and \
                                        isinstance(telefone,str) and \
                                            isinstance(cargo,str) and \
                                                isinstance(genero,str) :


            funcionario = Funcionario.query.filter_by(cpf=cpf).first()

            if funcionario:   #pelo id ser criado pelo sistema, essa verificação pode não se rnecessaria , então, usei o cpf.
                return {"code_status": "funcionario ja cadastrado" } , 400
            
            funcionario = Funcionario(nome=nome,
                                cpf=cpf,
                                email=email,
                                senha=senha,
                                endereço=endereço,
                                idade=idade,
                                salario=salario,
                                telefone=telefone,
                                cargo=cargo,
                                genero=genero)
            
            funcionario.save()
            #mandando email de confirmação de cadastro.
            msg = Message(sender= 'ianmeirelles@poli.ufrj.br',
            recipients=[email],subject='cadastro realizado',
            html= render_template('email.html', nome = nome))
            
            mail.send(msg)

            return funcionario.json(), 200

    def get(self):

        funcionarios = Funcionario.query.all()

        return jsonify([funcionario.json() for funcionario in funcionarios]) , 200

class funcionarioDetalhes(MethodView):            # a rota dela é /mudançafun

    def get(self, id):

        funcionario = Funcionario.query.get_or_404(id)

        return funcionario.json()


    def put(self , id) :

        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        
        nome = body.get('nome')
        cpf=body.get('cpf')
        email = body.get('email')
        senha = body.get('senha')
        endereço = body.get('endereço') 
        idade=body.get('idade')
        salario=body.get('salario')
        telefone=body.get('telefone')
        cargo=body.get('cargo')
        genero=body.get('genero')

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(senha,str) and \
                            isinstance(endereço,str) and \
                                isinstance(idade,int) and \
                                    isinstance(salario,float) and \
                                        isinstance(telefone,str) and \
                                            isinstance(cargo,str) and \
                                                isinstance(genero,str) :
            
            funcionario.nome=nome
            funcionario.cpf=cpf
            funcionario.email=email
            funcionario.senha=senha
            funcionario.endereço=endereço
            funcionario.idade=idade
            funcionario.salario=salario
            funcionario.telefone=telefone
            funcionario.cargo=cargo
            funcionario.genero=genero


            funcionario.update()

            return funcionario.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    def patch(self , id) :

        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get('nome' ,funcionario.nome )
        cpf=body.get('cpf' ,funcionario.cpf )
        email = body.get('email' , funcionario.email )
        senha = body.get('senha' , funcionario.senha )
        endereço = body.get('endereço',funcionario.endereço ) 
        idade=body.get('idade',funcionario.idade )
        salario=body.get('salario',funcionario.salario )
        telefone=body.get('telefone',funcionario.telefone )
        cargo=body.get('cargo',funcionario.cargo )
        genero=body.get('genero',funcionario.genero )

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(senha,str) and \
                            isinstance(endereço,str) and \
                                isinstance(idade,int) and \
                                    isinstance(salario,float) and \
                                        isinstance(telefone,str) and \
                                            isinstance(cargo,str) and \
                                                isinstance(genero,str) :
            
            funcionario.nome=nome
            funcionario.cpf=cpf
            funcionario.email=email
            funcionario.senha=senha
            funcionario.endereço=endereço
            funcionario.idade=idade
            funcionario.salario=salario
            funcionario.telefone=telefone
            funcionario.cargo=cargo
            funcionario.genero=genero


            funcionario.update()

            return funcionario.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    
    def delete(self,id):

        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)

        return funcionario.json()

class Loginfun(MethodView): # rota /loginfun
    def post(self):

        body = request.json

        cpf = body.get("cpf") #nesse caso o login é pelo cpf
        senha = body.get("senha")

        funcionario = Funcionario.query.filter_by(cpf = cpf).first() 

        if funcionario and  bcrypt.checkpw(senha.encode() , funcionario.senha.encode()):
            return {"token":create_access_token(funcionario.id , additional_claims={"usuario":"logado"})}
        return {"msg":"cpf e/ou senha incorretos "} , 400 

        