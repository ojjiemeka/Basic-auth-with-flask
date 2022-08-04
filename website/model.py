from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(225), unique=True)
    password = db.Column(db.String(150))
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    notes = db.relationship('Note')
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
