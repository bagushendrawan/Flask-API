from . import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True )
    password = db.Column(db.String(64), nullable=False )
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())