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


class ModelUser(object):
    def __init__(self, user_login=None, user_password=None):
        self.user_login = user_login
        self.user_password = user_password


class ModelGeolocation(object):
    def __init__(self, latitude=None, longitude=None, radius=None):
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius


class ModelNotification(object):
    def __init__(self, notification=None):
        self.notification = notification


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
