import os
from dotenv import load_dotenv

load_dotenv()

class config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    JWT_SECRET_KEY =os.getenv("SECRET_KEY")
    

    #MAIL_SERVER = sen.MAIL_SERVER
    #MAIL_PORT = sen.MAIL_PORT
    #MAIL_USERNAME = sen.MAIL_USERNAME
    #MAIL_PASSWORD = sen.MAIL_PASSWORD
    #MAIL_USE_TLS = sen.MAIL_USE_TLS
    #MAIL_USE_SSL = sen.MAIL_USE_SSL
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_ACCESS_KEY =os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
    AWS_PROJECT_NAME = os.getenv("AWS_PROJECT_NAME")
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_BUCKET_ENDPOINT = os.getenv("AWS_BUCKET_ENDPOINT")
