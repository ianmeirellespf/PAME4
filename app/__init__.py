from flask import Flask
from .config import config
from .extensions import db , migrate , mail , jwt

from app.cliente.routes import cliente_api
from app.unidade.routes import unidade_api
from app.produto.routes import produto_api
from app.funcionario.routes import funcionario_api
from app.venda.routes import venda_api



def create_app():

    app=Flask(__name__)

    app.config.from_object(config)

    
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    app.register_blueprint(cliente_api)
    app.register_blueprint(unidade_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(venda_api)
    
    


    return app