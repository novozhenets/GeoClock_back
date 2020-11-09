from flask import Flask
from gevent.pywsgi import WSGIServer
from markupsafe import escape

app = Flask(__name__)


@app.route('/ira/<test>')
def show_user_profile(test):
    return 'test =  %s' % escape(test)


server_gevent = WSGIServer(('127.0.0.1', 3000), app)
server_gevent.serve_forever()
