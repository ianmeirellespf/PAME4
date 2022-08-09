from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

mail = Mail()
db = SQLAlchemy()
migrate=Migrate()
jwt = JWTManager()
ma = Marshmallow()