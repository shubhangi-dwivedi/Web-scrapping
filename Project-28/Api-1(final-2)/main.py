from flask import Flask
from flask_restful import Api
from femi_api import returnjson

app = Flask(__name__)

api = Api(app)

api.add_resource(returnjson,'/')
#api.add_resource(readjson,'/a')


if __name__ == '__main__':
    app.run(debug = True)