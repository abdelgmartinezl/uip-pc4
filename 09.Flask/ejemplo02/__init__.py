from flask import Flask, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'millaveultrasecreta'

@app.route('/')
def index():
    if 'usuario' in session:
        usuario = session['usuario']
        return "Con la sesion de " + usuario + "<br>" + \
        "<b><a href='/salir'>Presione aqui para salir</a></b>"
    return "No tienes sesion <br><a href='/iniciar'></b>" + \
    "Haga clic aqui para iniciar sesion</b></a>"

@app.route('/iniciar', methods=['GET','POST'])
def iniciar():
    if request.method == 'POST':
        session['usuario'] = request.form['usuario']
        return redirect(url_for('index'))
    return '''
<form action="" method="post">
<p><input type=text name=usuario>
<p><input type=submit value=Iniciar>
</form>
'''

@app.route('/salir')
def salir():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()