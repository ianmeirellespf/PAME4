from app.venda.model import Venda
from flask import request , jsonify
from flask.views import MethodView

class vendaCreate(MethodView):  # a rota dela é /registroven

    def post(self):

        body = request.json

        
        valor = body.get('valor')
        data= body.get('data')
        avaliaçao=body.get('avaliaçao')
        delivery = body.get('delivery')
                

        if  isinstance(valor,float) and \
                isinstance(data,str) and \
                    isinstance(avaliaçao,float) and \
                        isinstance(delivery,bool)   :


            # venda = Venda.query.filter_by('algo'='algo').first()  "nao tem necessidade d eimpedir compras iguais , mas caso no futuro queiram, aqui está"

           # if venda:   #pelo id ser criado pelo sistema, essa verificação pode não ser necessaria , então, usei o lote.
           #     return {"code_status": "venda ja cadastrado" } , 400
            
            venda = Venda(valor=valor,
                                data=data,
                                avaliaçao=avaliaçao,
                                delivery=delivery)
            
            venda.save()

            return venda.json(), 200

    def get(self):

        vendas = Venda.query.all()

        return jsonify([venda.json() for venda in vendas]) , 200

class vendaDetalhes(MethodView):            # a rota dela é /mudançaven

    def get(self, id):

        venda = Venda.query.get_or_404(id)

        return venda.json()


    def put(self , id) :

        body = request.json
        venda = Venda.query.get_or_404(id)


       
        valor = body.get('valor')
        data= body.get('data')
        avaliaçao=body.get('avaliaçao')
        delivery = body.get('delivery')

        if  isinstance(valor,float) and \
                isinstance(data,str) and \
                    isinstance(avaliaçao,float) and \
                        isinstance(delivery,bool)   :
            
            venda.valor=valor
            venda.data=data
            venda.avaliaçao=avaliaçao
            venda.delivery=delivery
            
            


            venda.update()

            return venda.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    def patch(self , id) :

        body = request.json
        venda = Venda.query.get_or_404(id)

        valor = body.get('valor', venda.valor)
        data= body.get('data', venda.data)
        avaliaçao=body.get('avaliaçao', venda.avaliaçao)
        delivery = body.get('delivery', venda.delivery)

        if  isinstance(valor,float) and \
                isinstance(data,str) and \
                    isinstance(avaliaçao,float) and \
                        isinstance(delivery,bool)   :
            
            venda.valor=valor
            venda.data=data
            venda.avaliaçao=avaliaçao
            venda.delivery=delivery
            
            


            venda.update()

            return venda.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    
    def delete(self,id):

        venda = Venda.query.get_or_404(id)
        venda.delete(venda)

        return venda.json()