from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*":{"origins":"*"}})

class HelloWorld(Resource):
    def get(self):
        return {'message' : 'Hello World'}

class Greeting(Resource):
    def get(self):
        return {'greeting': 'happy holidays!'}


api.add_resource(HelloWorld, '/hello')
api.add_resource(Greeting, '/greeting')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)