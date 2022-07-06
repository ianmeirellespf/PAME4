from app.unidade.model import unidade_api
from app.unidade.controler import unidadeCreate , unidadeDetalhes

unidade_api.add_url_rule('/registro', view_func= unidadeCreate.as_view("cria_unidade") , methods = ['POST' , 'GET'])
unidade_api.add_url_rule('/mudança', view_func= unidadeDetalhes.as_view("muda_unidade") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])