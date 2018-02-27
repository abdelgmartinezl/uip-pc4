from flask import Flask, redirect, url_for
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

@app.route('/admin')
def saludar_admin():
    return 'Maestro en jefe, saludos...'

@app.route('/invitado/<invitado>')
def saludar_invitado(invitado):
    return 'Hola, %s, conoces a Petra?' % invitado

@app.route('/usuario/<nombre>')
def saludar_usuario(nombre):
    if nombre == 'admin':
        return redirect(url_for('saludar_admin'))
    else:
        return redirect(url_for('saludar_invitado', 
            invitado=nombre))

if __name__ == '__main__':
    app.run()