from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'wololo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['usuario'] != 'admin' or request.form['contrasena'] != 'admin':
            error = 'Usuario o contrasena invalida. Intente nuevamente!'
        else:
            flash('Inicio sesion con exito')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run()