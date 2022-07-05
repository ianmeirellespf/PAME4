from flask import Flask
from .config import config
from .extensions import db , migrate

from app.class1.model import classe1_api
from app.class2.model import class2_api



def create_app():

    app=Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(classe1_api)
    app.register_blueprint(class2_api)
    


    return app