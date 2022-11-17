from flask import Flask
from flask_restful import Api
from femi_api import femina

app = Flask(__name__)

api = Api(app)

api.add_resource(femina,'/femina')

if __name__ == '__main__':
    app.run(debug = True)