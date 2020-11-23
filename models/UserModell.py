from app import db


class User(db.Model):
    user_login = db.Column(db.String(50), primary_key=True)
    user_password = db.Column(db.String(50), primary_key=True)
