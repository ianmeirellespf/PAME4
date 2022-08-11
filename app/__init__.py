from flask import Flask
from .config import config
from .extensions import db , migrate , mail , jwt

from app.user.routes import user_api




def create_app():

    app=Flask(__name__)

    app.config.from_object(config)

    
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    app.register_blueprint(user_api)
    
    
    


    return app