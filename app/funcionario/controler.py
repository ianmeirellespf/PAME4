from app.funcionario.model import Funcionario
from flask import request , jsonify
from flask.views import MethodView

class funcionarioCreate(MethodView):  # a rota dela é /registro

    def post(self):

        body = request.json

        id = body.get('id')
        nome = body.get('nome')
        cpf=body.get('cpf')
        email = body.get('email')
        endereço = body.get('endereço') 
        idade=body.get('idade')
        salario=body.get('salario')
        telefone=body.get('telefone')
        cargo=body.get('cargo')
        genero=body.get('genero')
        

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
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
                                endereço=endereço,
                                idade=idade,
                                salario=salario,
                                telefone=telefone,
                                cargo=cargo,
                                genero=genero)
            
            funcionario.save()

            return funcionario.json(), 200

    def get(self):

        funcionarios = Funcionario.query.all()

        return jsonify([funcionario.json() for funcionario in funcionarios]) , 200

class funcionarioDetalhes(MethodView):            # a rota dela é /mudança

    def get(self, id):

        funcionario = Funcionario.query.get_or_404(id)

        return funcionario.json()


    def put(self , id) :

        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        
        nome = body.get('nome')
        cpf=body.get('cpf')
        email = body.get('email')
        endereço = body.get('endereço') 
        idade=body.get('idade')
        salario=body.get('salario')
        telefone=body.get('telefone')
        cargo=body.get('cargo')
        genero=body.get('genero')

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(endereço,str) and \
                            isinstance(idade,int) and \
                                isinstance(salario,float) and \
                                    isinstance(telefone,str) and \
                                        isinstance(cargo,str) and \
                                            isinstance(genero,str) :
            
            funcionario.nome=nome
            funcionario.cpf=cpf
            funcionario.email=email
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
        endereço = body.get('endereço',funcionario.endereço ) 
        idade=body.get('idade',funcionario.idade )
        salario=body.get('salario',funcionario.salario )
        telefone=body.get('telefone',funcionario.telefone )
        cargo=body.get('cargo',funcionario.cargo )
        genero=body.get('genero',funcionario.genero )

        if  isinstance(nome,str) and \
                isinstance(cpf,str) and \
                    isinstance(email,str) and \
                        isinstance(endereço,str) and \
                            isinstance(idade,int) and \
                                isinstance(salario,float) and \
                                    isinstance(telefone,str) and \
                                        isinstance(cargo,str) and \
                                            isinstance(genero,str) :
            
            funcionario.nome=nome
            funcionario.cpf=cpf
            funcionario.email=email
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