from app.model import BaseModel
from app.extensions import db

class File(BaseModel):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    media_path = db.Column(db.String(300))
    title = db.Column(db.String(100))
    