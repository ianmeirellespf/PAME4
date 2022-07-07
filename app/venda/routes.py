
from app.venda.controler import vendaCreate , vendaDetalhes
from flask import Blueprint

venda_api = Blueprint("venda_api", __name__)

venda_api.add_url_rule('/registroven', view_func= vendaCreate.as_view("cria_venda") , methods = ['POST' , 'GET'])
venda_api.add_url_rule('/mudançaven', view_func= vendaDetalhes.as_view("muda_venda") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])