from flask import Flask
from .config import config
from .extensions import db , migrate

from app.cliente.model import cliente_api
from app.unidade.model import unidade_api
from app.produto.model import produto_api
from app.funcionario.model import funcionario_api
from app.vendas.model import venda_api



def create_app():

    app=Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(unidade_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(venda_api)
    
    


    return app