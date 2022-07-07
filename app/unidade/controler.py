
from app.unidade.model import Unidade
from flask import request , jsonify
from flask.views import MethodView

class unidadeCreate(MethodView):  # a rota dela é /registrouni

    def post(self):

        body = request.json

       
        nome = body.get('nome')
        endereço=body.get('endereço')
        receita=body.get('receita')
        lucro=body.get('lucro')
        horaAbre=body.get('horaAbre')
        horaFecha=body.get('horaFecha')
            

        if  isinstance(nome,str) and \
                isinstance(endereço,str) and \
                    isinstance(receita,float) and \
                        isinstance(lucro,float) and \
                            isinstance(horaAbre,str) and \
                                isinstance(horaFecha,str)  :


            unidade = Unidade.query.filter_by(endereço=endereço).first()

            if unidade:   #pelo id ser criado pelo sistema, essa verificação pode não ser necessaria , então, usei o lote.
                return {"code_status": "unidade ja cadastrado" } , 400
            
            unidade = Unidade(nome=nome,
                                endereço=endereço,
                                receita=receita,
                                lucro=lucro,
                                horaAbre=horaAbre,
                                horaFecha=horaFecha)
            
            unidade.save()

            return unidade.json(), 200

    def get(self):

        unidades = Unidade.query.all()

        return jsonify([unidade.json() for unidade in unidades]) , 200

class unidadeDetalhes(MethodView):            # a rota dela é /mudançauni

    def get(self, id):

        unidade = Unidade.query.get_or_404(id)

        return unidade.json()


    def put(self , id) :

        body = request.json
        unidade = Unidade.query.get_or_404(id)


        nome = body.get('nome')
        endereço=body.get('endereço')
        receita=body.get('receita')
        lucro=body.get('lucro')
        horaAbre=body.get('horaAbre')
        horaFecha=body.get('horaFecha')

        if  isinstance(nome,str) and \
                isinstance(endereço,str) and \
                    isinstance(receita,float) and \
                        isinstance(lucro,float) and \
                            isinstance(horaAbre,str) and \
                                isinstance(horaFecha,str)  :

            
            unidade.nome=nome
            unidade.endereço=endereço
            unidade.receita=receita
            unidade.lucro=lucro
            unidade.horaAbre=horaAbre
            unidade.horaFecha=horaFecha
            


            unidade.update()

            return unidade.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    def patch(self , id) :

        body = request.json
        unidade = Unidade.query.get_or_404(id)

        nome = body.get('nome',unidade.nome)
        endereço=body.get('endereço',unidade.endereço)
        receita=body.get('receita',unidade.receita)
        lucro=body.get('lucro',unidade.lucro)
        horaAbre=body.get('horaAbre',unidade.horaAbre)
        horaFecha=body.get('horaFecha',unidade.horaFecha)

        if  isinstance(nome,str) and \
                isinstance(endereço,str) and \
                    isinstance(receita,float) and \
                        isinstance(lucro,float) and \
                            isinstance(horaAbre,str) and \
                                isinstance(horaFecha,str)  :
            
            unidade.nome=nome
            unidade.endereço=endereço
            unidade.receita=receita
            unidade.lucro=lucro
            unidade.horaAbre=horaAbre
            unidade.horaFecha=horaFecha

            unidade.update()

            return unidade.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    
    def delete(self,id):

        unidade = Unidade.query.get_or_404(id)
        unidade.delete(unidade)

        return unidade.json()