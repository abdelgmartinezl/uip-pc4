from flask import Flask
from flask_restful import Api, Resource
from flask_restful import reqparse
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'uip'
app.config['MYSQL_DATABASE_PASSWORD'] = 'uip'
app.config['MYSQL_DATABASE_DB'] = 'articulos'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

class CrearUsuario(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('correo', type=str, help='Correo electronico')
            parser.add_argument('passwd', type=str, help='Contraseña')
            args = parser.parse_args()
            _correo = args['correo']
            _passwd = args['passwd']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spCrearUsuario', (_correo,_passwd))
            resultado = cursor.fetchall()

            if len(resultado) is 0:
                conn.commit()
                return {'estado': '200', 'mensaje': 'Usuario creado exitosamente'}
            else:
                return {'estado': '1234', 'mensaje': str(resultado[0])}

        except Exception as e:
            return {'error': str(e)}

class AutenticarUsuario(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('correo', type=str, help='Correo electronico')
            parser.add_argument('passwd', type=str, help='Contraseña')
            args = parser.parse_args()
            _correo = args['correo']
            _passwd = args['passwd']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spAutenticarUsuario', (_correo,))
            resultado = cursor.fetchall()

            if len(resultado) > 0:
                if str(resultado[0][2]) == _passwd:
                    return {'estado': 200, 'id': str(resultado[0][0])}
                else:
                    return {'estado': 176, 'mensaje': "¡Autenticacion fallida!"}

        except Exception as e:
            return {'error': str(e)}

class AgregarArticulos(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_usuario', type=str)
            parser.add_argument('articulo', type=str)
            args = parser.parse_args()
            _id_usuario = args['id_usuario']
            _articulo = args['articulo']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spAgregarArticulos', (_id_usuario,_articulo))
            resultado = cursor.fetchall()

            conn.commit()
            return {'estado': '200', 'mensaje': 'Exitoso'}

        except Exception as e:
            return {'error': str(e)}

class ObtenerArticulos(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_usuario', type=str)
            args = parser.parse_args()
            _id_usuario = args['id_usuario']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spObtenerArticulos', (_id_usuario,))
            resultado = cursor.fetchall()

            lista_articulos = []
            for articulo in resultado:
                i = {
                    'id': articulo[0],
                    'articulo': articulo[1]
                }
                lista_articulos.append(i)

            return {'estado': '200', 'articulos': lista_articulos}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(CrearUsuario, '/usuario')
api.add_resource(AutenticarUsuario, '/autenticacion')
api.add_resource(AgregarArticulos, '/articulo')
api.add_resource(ObtenerArticulos, '/articulos')


if __name__ == "__main__":
    app.run(debug=True)
