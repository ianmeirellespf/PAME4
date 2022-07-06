from crypt import methods
from app.cliente.model import cliente_api
from app.cliente.controler import clienteCreate , clienteDetalhes

cliente_api.add_url_rule('/registro', view_func= clienteCreate.as_view("cria_cliente") , methods = ['POST' , 'GET'])
cliente_api.add_url_rule('/mudança', view_func= clienteDetalhes.as_view("muda_cliente") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])


