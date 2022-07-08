
from app.cliente.controler import clienteCreate , clienteDetalhes , Logincli
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

cliente_api.add_url_rule('/registrocli', view_func= clienteCreate.as_view("cria_cliente") , methods = ['POST' , 'GET'])
cliente_api.add_url_rule('/mudançacli', view_func= clienteDetalhes.as_view("muda_cliente") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])
cliente_api.add_url_rule('/logincli', view_func= Logincli.as_view("loga_cliente") , methods = ['POST'])


