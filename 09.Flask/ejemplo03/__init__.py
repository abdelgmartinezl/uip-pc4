from flask import Flask, render_template, url_for, redirect, request, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['usuario'] == 'admin':
            return redirect(url_for('exito'))
        else:
            abort(401)
# 400 bad request
# 401 unauthenticated
# 403 forbidden
# 404 not found
# 406 not acceptable
# 415 tipo no soportado
# 429 demasiadas peticiones
    return redirect(url_for('index'))

@app.route('/exito')
def exito():
    return 'Estas dentro'

if __name__ == '__main__':
    app.run()