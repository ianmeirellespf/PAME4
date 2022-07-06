from app.funcionario.model import funcionario_api
from app.funcionario.controler import funcionarioCreate , funcionarioDetalhes

funcionario_api.add_url_rule('/registro', view_func= funcionarioCreate.as_view("cria_funcionario") , methods = ['POST' , 'GET'])
funcionario_api.add_url_rule('/mudança', view_func= funcionarioDetalhes.as_view("muda_funcionario") , methods = ['GET' , 'PUT' , 'PATCH' , 'DELETE'])