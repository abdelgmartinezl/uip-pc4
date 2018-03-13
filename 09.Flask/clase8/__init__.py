from flask import Flask, render_template
app = Flask(__name__)

@app.route('/evaluador/<int:nota>')
def evaluador(nota):
    return render_template('evaluador.html', calificacion=nota)

@app.route('/resultado')
def resultado():
    notas = {'ing': 77, 'cal': 85, 'pc4': 100}
    return render_template('resultado.html', result=notas)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()