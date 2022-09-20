from flask import Flask
from .config import config
from .extensions import db , migrate , mail , jwt , ma


from app.user.routes import user_api
from app.auth.routes import auth_api
from app.file.routes import file_api
from app.storageDireto.routes import storageDireto_api




def create_app():

    app=Flask(__name__)

    app.config.from_object(config)

    
    db.init_app(app)
    
    mail.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    ma.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(auth_api)
    app.register_blueprint(storageDireto_api)
    app.register_blueprint(file_api)
   
    
    
    


    return app