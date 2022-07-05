from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

classe1_api = Blueprint("classe1_api", __name__)



class class1(BaseModel):

    __tablename__ = "classe1"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    