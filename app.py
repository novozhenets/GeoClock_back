from flask import Flask, json
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def db_create():
    db.create_all()


@app.route("/start")
def Hello():
    return "Hello to everyoneeee!"


class User(db.Model):
    user_login = db.Column(db.String(50), primary_key=True)
    user_password = db.Column(db.String(50), primary_key=True)


class Geolocation(db.Model):
    latitude = db.Column(db.Float, primary_key=True)
    longitude = db.Column(db.Float, primary_key=True)
    radius = db.Column(db.Integer, primary_key=True)


class Notification(db.Model):
    notification = db.Column(db.String(200), primary_key=True)


class UserController(object):
    def __init__(self, model_user):
        self.model_user = model_user


class GeolocationController(object):
    def __init__(self, model_geolocation):
        self.model_geolocation = model_geolocation


class NotificationController(object):
    def __init__(self, model_notification):
        self.model_notification = model_notification


if __name__ == '__main__':
    manager.run()