from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Rabotyahy!'

@app.route('/Anastasia')
def hello_world():
    return 'Good luck!'

if __name__ == '__main__':
    app.run()
