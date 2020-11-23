from app import db


class Notification(db.Model):
    notification = db.Column(db.String(200), primary_key=True)
