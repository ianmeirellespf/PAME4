from app.extensions import db
from app.model import BaseModel

class Professor(BaseModel) :

    _tablename_= 'professor'

    id = db.Column(db.Integer , primary_Key = True , autoincrement = True)

    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    user = db.Relationship ("User", back_populates = 'professor')