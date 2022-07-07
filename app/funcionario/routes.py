from app.funcionario.controler import funcionarioCreate , funcionarioDetalhes
from flask import Blueprint

funcionario_api = Blueprint("funcionario_api", __name__)

funcionario_api.add_url_rule('/registrofun', view_func= funcionarioCreate.as_view("cria_funcionario") , methods = ['POST' , 'GET'])
funcionario_api.add_url_rule('/mudançafun', view_func= funcionarioDetalhes.as_view("muda_funcionario") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])