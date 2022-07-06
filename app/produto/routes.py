from app.produto.model import produto_api
from app.produto.controler import produtoCreate , produtoDetalhes

produto_api.add_url_rule('/registro', view_func= produtoCreate.as_view("cria_produto") , methods = ['POST' , 'GET'])
produto_api.add_url_rule('/mudança', view_func= produtoDetalhes.as_view("muda_produto") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])