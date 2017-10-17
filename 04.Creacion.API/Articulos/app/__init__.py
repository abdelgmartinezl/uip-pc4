from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class CrearUsuario(Resource):
    def post(self):
        return {'estado': 'exitoso'}

api.add_resource(CrearUsuario, '/usuario')

if __name__ == "__main__":
    app.run(debug=True)