from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    usertype = db.Column(db.String(120))
    aboutuni = db.Column(db.String(1000))
    instituteimg = db.Column(db.String(1000))
    institutelogo = db.Column(db.String(1000))
    maths = db.Column(db.String(150))
    english = db.Column(db.String(150))
    maltese = db.Column(db.String(150))
    computer_studies = db.Column(db.String(150))
    biology = db.Column(db.String(150))
    physics = db.Column(db.String(150))
    chemistry = db.Column(db.String(150))
    italian = db.Column(db.String(150))
    french = db.Column(db.String(150))
    home_economics = db.Column(db.String(150))
    accounts = db.Column(db.String(150))
    courses = db.relationship('Courses')


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(300))
    institute = db.Column(db.String(300))
    neededSubject = db.Column(db.String(300))
    about = db.Column(db.String(1000))
    courseimg = db.Column(db.String(1000))
    modules = db.Column(db.String(300))
    careers = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

