from flask import Flask
from .config import config
from .extensions import db , migrate

from app.cliente.model import cliente_api
from app.entrega.model import entrega_api
from app.entregador.model import entregador_api
from app.produto.model import produto_api
from app.supermercado.model import supermercado_api
from app.suporte.model import suporte_api


def create_app():

    app=Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(entrega_api)
    app.register_blueprint(entregador_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(supermercado_api)
    app.register_blueprint(suporte_api)


    return app