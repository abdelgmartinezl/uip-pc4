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

api.add_resource(CrearUsuario, '/usuario')

if __name__ == "__main__":
    app.run(debug=True)
