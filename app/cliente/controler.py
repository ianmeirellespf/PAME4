from app.cliente.model import Cliente
from flask import render_template, request , jsonify
from flask_jwt_extended import create_access_token
from flask.views import MethodView
from flask_mail import Message
from app.extensions import mail
import bcrypt


class clienteCreate(MethodView):  # a rota dela é /registrocli
                                  #no codigo , a senha está sendo tratado como um codigo qualquer por enquanto, mas será privado.
    def post(self):

        body = request.json

        
        nome = body.get('nome')
        cpf=body.get('cpf')
        email = body.get('email')
        senha = body.get('senha')
        senha = bcrypt.hashpw(senha.encode() , bcrypt.gensalt()).decode() #tornando a senha em criptografia  e adicionando o salt, para não atrapalhar senhas iguais em caso de hacker.
        endereço = body.get('endereço') 
        idade=body.get('idade')
        genero=body.get('genero')
        

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(endereço,str) and \
                            isinstance(senha,str) and \
                                isinstance(idade,int) and \
                                    isinstance(genero,str) :


            cliente = Cliente.query.filter_by(cpf=cpf).first()

            if cliente:   #pelo id ser criado pelo sistema, essa verificação pode não se rnecessaria , mas decidi colocar.
                return {"code_status": "Cliente ja cadastrado" } , 400
            
            cliente = Cliente(nome=nome,
                                cpf=cpf,
                                email=email,
                                senha=senha,
                                endereço=endereço,
                                idade=idade,
                                genero=genero)
            
            cliente.save()
            #mandando email de confirmação de cadastro.
            msg = Message(sender= 'ianmeirelles@poli.ufrj.br',
            recipients=[email],subject='cadastro realizado',
            html= render_template('email.html', nome = nome))
            
            mail.send(msg)

            return cliente.json(), 200

    def get(self):

        clientes = Cliente.query.all()

        return jsonify([cliente.json() for cliente in clientes]) , 200

class clienteDetalhes(MethodView):            # a rota dela é /mudançacli

    def get(self, id):

        cliente = Cliente.query.get_or_404(id)

        return cliente.json()


    def put(self , id) :

        body = request.json
        cliente = Cliente.query.get_or_404(id)

        nome = body.get('nome')
        cpf=body.get('cpf')
        email = body.get('email')
        senha = body.get('senha')
        endereço = body.get('endereço') 
        idade=body.get('idade')
        genero=body.get('genero')

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(endereço,str) and \
                            isinstance(senha,str) and \
                                isinstance(idade,int) and \
                                    isinstance(genero,str) :
            
            cliente.nome=nome
            cliente.cpf=cpf
            cliente.email=email
            cliente.senha=senha
            cliente.endereço=endereço
            cliente.idade=idade
            cliente.genero=genero

            cliente.update()

            return cliente.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    def patch(self , id) :

        body = request.json
        cliente = Cliente.query.get_or_404(id)

        nome = body.get('nome' , cliente.nome)
        cpf=body.get('cpf', cliente.cpf)
        email = body.get('email', cliente.email)
        senha = body.get('senha', cliente.senha)
        endereço = body.get('endereço', cliente.endereço) 
        idade=body.get('idade', cliente.idade)
        genero=body.get('genero', cliente.genero)

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(endereço,str) and \
                            isinstance(senha,str) and \
                                isinstance(idade,int) and \
                                    isinstance(genero,str) :
            
            cliente.nome=nome
            cliente.cpf=cpf
            cliente.email=email
            cliente.senha=senha
            cliente.endereço=endereço
            cliente.idade=idade
            cliente.genero=genero

            cliente.update()

            return cliente.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    
    def delete(self,id):

        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)

        return cliente.json()


class Logincli(MethodView):     # rota /logincli
    def post(self):

        body = request.json

        cpf = body.get("cpf") #nesse caso o login é pelo cpf
        senha = body.get("senha")

        cliente = Cliente.query.filter_by(cpf = cpf).first()

        if  cliente and bcrypt.checkpw(senha.encode() , cliente.senha.encode()):
            return {"token":create_access_token(cliente.id , additional_claims={"usuario":"logado"})}
        return {"msg":"cpf e/ou senha incorretos"} , 400

        

        



        




