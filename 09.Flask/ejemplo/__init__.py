from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# @app.route('/')
# def choteo():
#     return 'Xopa moh!'

# @app.route('/saludar')
# def saludar():
#     return 'Saludos cordiales!'

# @app.route('/saludar/<nombre>')
# def saludar_nombre(nombre):
#     return 'Saludos, %s!' % nombre

# @app.route('/calculadora/<int:a>')
# def calcular_itbms(a):
#     return str(a*1.07)

# @app.route('/calculadora/<float:a>')
# def calcular_itbms2(a):
#     return str(a*1.07)

# @app.route('/admin')
# def saludar_admin():
#     return 'Maestro en jefe, saludos...'

# @app.route('/invitado/<invitado>')
# def saludar_invitado(invitado):
#     return 'Hola, %s, conoces a Petra?' % invitado

# @app.route('/usuario/<nombre>')
# def saludar_usuario(nombre):
#     if nombre == 'admin':
#         return redirect(url_for('saludar_admin'))
#     else:
#         return redirect(url_for('saludar_invitado', 
#             invitado=nombre))

# @app.route('/vive')
# def vivir():
#     return 'Puedes vivir en Brazil'

# @app.route('/muere')
# def morir():
#     return 'Cuidado con irte a Brazil'

# @app.route('/brasil', methods=['POST', 'GET'])
# def brasil():
#     if request.method == 'POST':
#         salario = float(request.form['sm'])
#         if salario > 3750.0:
#             return redirect(url_for('vivir'))
#         else:
#             return redirect(url_for('morir'))
#     else:
#         return 'Para que quieres ir?'

@app.route('/html')
def inicio():
    return '<html><body><h1>Xopa</h1></body></html>'

@app.route('/')
def indice():
    return render_template('hola.html')

@app.route('/usuario/<usuario>')
def chotear_usuario(usuario):
    return render_template('hola2.html', nombre=usuario)

if __name__ == '__main__':
    app.run()