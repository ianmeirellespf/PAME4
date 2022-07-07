
from app.produto.controler import produtoCreate , produtoDetalhes
from flask import Blueprint

produto_api = Blueprint("produto_api", __name__)

produto_api.add_url_rule('/registropro', view_func= produtoCreate.as_view("cria_produto") , methods = ['POST' , 'GET'])
produto_api.add_url_rule('/mudançapro', view_func= produtoDetalhes.as_view("muda_produto") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])