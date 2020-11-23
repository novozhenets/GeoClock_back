from app import db


class Geolocation(db.Model):
    latitude = db.Column(db.Float, primary_key=True)
    longitude = db.Column(db.Float, primary_key=True)
    radius = db.Column(db.Integer, primary_key=True)
