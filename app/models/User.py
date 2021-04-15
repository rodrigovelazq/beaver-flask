from app import db
from .Role import user_role

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary=user_role)

    def __repr__(self):
        return f"User('{self.username}','{self.firstname}','{self.lastname}')"
