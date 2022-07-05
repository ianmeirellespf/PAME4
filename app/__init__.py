from flask import Flask
from .config import config
from .extensions import db , migrate

from app.cliente.model import cliente_api
from app.unidade.model import unidade_api



def create_app():

    app=Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(unidade_api)
    


    return app