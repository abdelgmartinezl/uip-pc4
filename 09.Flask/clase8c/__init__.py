from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarcookie', methods=['POST'])
def guardarcookie():
    if request.method == 'POST':
        id = request.form['id']
        respuesta = make_response(render_template('leercookie.html'))
        respuesta.set_cookie('id', id)
        return respuesta

@app.route('/buscarcookie')
def buscarcookie():
    id = request.cookies.get('id')
    return '<h1>Bienvenido ' + id + '</h1>'

if __name__ == "__main__":
    app.run()