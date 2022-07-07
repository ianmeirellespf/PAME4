
from app.produto.model import Produto
from flask import request , jsonify
from flask.views import MethodView

class produtoCreate(MethodView):  # a rota dela é /registropro

    def post(self):

        body = request.json

        
        nome = body.get('nome')
        valor = body.get('valor')
        estoque= body.get('estoque')
        validade = body.get('validade')
        marca = body.get('marca')
        localEstoque = body.get('localEstoque')     
        localBalcao = body.get('localBalcao')
        categoria = body.get('categoria')
        receita = body.get('receita')
        lote = body.get('lote')
            

        if  isinstance(nome,str) and \
                isinstance(valor,float) and \
                    isinstance(estoque,int) and \
                        isinstance(validade,str) and \
                            isinstance(marca,str) and \
                                isinstance(localEstoque,str) and \
                                    isinstance(localBalcao,str) and \
                                        isinstance(categoria,str) and \
                                            isinstance(receita,bool) and \
                                                  isinstance(lote,str) :


            produto = Produto.query.filter_by(lote=lote).first()

            if produto:   #pelo id ser criado pelo sistema, essa verificação pode não ser necessaria , então, usei o lote.
                return {"code_status": "produto ja cadastrado" } , 400
            
            produto = Produto(nome=nome,
                                valor=valor,
                                estoque=estoque,
                                validade=validade,
                                marca=marca,
                                localEstoque=localEstoque,
                                localBalcao=localBalcao,
                                categoria=categoria,
                                receita=receita,
                                lote = lote)
            
            produto.save()

            return produto.json(), 200

    def get(self):

        produtos = Produto.query.all()

        return jsonify([produto.json() for produto in produtos]) , 200

class produtoDetalhes(MethodView):            # a rota dela é /mudançapro

    def get(self, id):

        produto = Produto.query.get_or_404(id)

        return produto.json()


    def put(self , id) :

        body = request.json
        produto = Produto.query.get_or_404(id)


        nome = body.get('nome')
        valor = body.get('valor')
        estoque= body.get('estoque')
        validade = body.get('validade')
        marca = body.get('marca')
        localEstoque = body.get('localEstoque')     
        localBalcao = body.get('localBalcao')
        categoria = body.get('categoria')
        receita = body.get('receita')
        lote = body.get('lote')

        if  isinstance(nome,str) and \
                isinstance(valor,float) and \
                    isinstance(estoque,int) and \
                        isinstance(validade,str) and \
                            isinstance(marca,str) and \
                                isinstance(localEstoque,str) and \
                                    isinstance(localBalcao,str) and \
                                        isinstance(categoria,str) and \
                                            isinstance(receita,bool) and \
                                                  isinstance(lote,str) :
            
            produto.nome=nome
            produto.valor=valor
            produto.estoque=estoque
            produto.validade=validade
            produto.marca=marca
            produto.localEstoque=localEstoque
            produto.localBalcao=localBalcao
            produto.categoria=categoria
            produto.receita=receita
            produto.lote=lote


            produto.update()

            return produto.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    def patch(self , id) :

        body = request.json
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome', produto.nome)
        valor = body.get('valor', produto.valor)
        estoque= body.get('estoque', produto.estoque)
        validade = body.get('validade', produto.validade)
        marca = body.get('marca', produto.marca)
        localEstoque = body.get('localEstoque', produto.localEstoque)     
        localBalcao = body.get('localBalcao', produto.localBalcao)
        categoria = body.get('categoria', produto.categoria)
        receita = body.get('receita', produto.receita)
        lote = body.get('lote', produto.lote)

        if  isinstance(nome,str) and \
                isinstance(valor,float) and \
                    isinstance(estoque,int) and \
                        isinstance(validade,str) and \
                            isinstance(marca,str) and \
                                isinstance(localEstoque,str) and \
                                    isinstance(localBalcao,str) and \
                                        isinstance(categoria,str) and \
                                            isinstance(receita,bool) and \
                                                  isinstance(lote,str) :
            
            produto.nome=nome
            produto.valor=valor
            produto.estoque=estoque
            produto.validade=validade
            produto.marca=marca
            produto.localEstoque=localEstoque
            produto.localBalcao=localBalcao
            produto.categoria=categoria
            produto.receita=receita
            produto.lote=lote

            produto.update()

            return produto.json(), 200

        else :
            return {"code_status" : "dados invalidos"} , 400

    
    def delete(self,id):

        produto = Produto.query.get_or_404(id)
        produto.delete(produto)

        return produto.json()