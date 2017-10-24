from nest import nest
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return nest.go_spidey()

api.add_resource(HelloWorld, '/status')

if __name__ == '__main__':
    app.run(debug=True)
