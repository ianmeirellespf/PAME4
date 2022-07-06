from app.venda.model import venda_api
from app.venda.controler import vendaCreate , vendaDetalhes

venda_api.add_url_rule('/registro', view_func= vendaCreate.as_view("cria_venda") , methods = ['POST' , 'GET'])
venda_api.add_url_rule('/mudança', view_func= vendaDetalhes.as_view("muda_venda") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])