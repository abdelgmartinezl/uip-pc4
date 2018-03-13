from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def comision():
     return render_template('comision.html')

@app.route('/resultado', methods=['POST', 'GET'])
def mostrar():
    if request.method == 'POST':
        resultado = request.form
        return render_template("tabla.html", r=resultado)
    else:
        return '<h1>INVALIDO</h1>'

if __name__ ==  '__main__':
    app.run()
    