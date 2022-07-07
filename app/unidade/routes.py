
from app.unidade.controler import unidadeCreate , unidadeDetalhes
from flask import Blueprint

unidade_api = Blueprint("unidade_api", __name__)

unidade_api.add_url_rule('/registrouni', view_func= unidadeCreate.as_view("cria_unidade") , methods = ['POST' , 'GET'])
unidade_api.add_url_rule('/mudançauni', view_func= unidadeDetalhes.as_view("muda_unidade") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])