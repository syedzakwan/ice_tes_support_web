from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
   
class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(1000))
    summary = db.Column(db.String(10000))
    start_date = db.Column(db.String(100))
    status = db.Column(db.String(100))
    help_needed = db.Column(db.String(10000))
    remark = db.Column(db.String(10000))