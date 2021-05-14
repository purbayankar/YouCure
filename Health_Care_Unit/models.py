from . import db
from flask_login import UserMixin

class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pwd = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Patient %r>' % self.email