from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

class2_api = Blueprint("class2_api", __name__)

class classe2(BaseModel):

    __tablename__ = "classe2"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    