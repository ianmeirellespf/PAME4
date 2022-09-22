import os
from dotenv import load_dotenv

load_dotenv()

class config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"#os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    JWT_SECRET_KEY =os.getenv("SECRET_KEY")
    

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    

    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_ACCESS_KEY =os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
    AWS_PROJECT_NAME = os.getenv("AWS_PROJECT_NAME")
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_BUCKET_ENDPOINT = os.getenv("AWS_BUCKET_ENDPOINT")
