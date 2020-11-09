from flask import Flask, request

app = Flask(__name__)


@app.route('/Vika', methods=['GET'])
def hello_world():
    lon=request.args.get('lon')
    lat=request.args.get('lat')
    return 'Your placement :  • longitude = ' + lon + '    •latitude = ' + lat


if __name__ == '__main__':
    app.run()
