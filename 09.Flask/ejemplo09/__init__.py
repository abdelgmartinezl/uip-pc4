from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basedato.db'
app.config['SECRET_KEY'] = 'wololo'

db = SQLAlchemy(app)
class Estudiante(db.Model):
    id = db.Column('id_estudiante', db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(200))
    ciudad = db.Column(db.String(50))
    pin = db.Column(db.String(10))
    def __init__(self, nombre, direccion, ciudad, pin):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.pin = pin

@app.route('/')
def mostrar():
    return render_template('mostrar.html', estudiantes = Estudiante.query.all())

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        if not request.form['nombre'] or not request.form['ciudad'] or not request.form['direccion']:
            flash('Introduzca todos los campos', 'error')
        else:
            estudiante = Estudiante(request.form['nombre'],
                                    request.form['direccion'],
                                    request.form['ciudad'],
                                    request.form['pin'])
            db.session.add(estudiante)
            db.session.commit()
            flash('Registro guardado exitosamente')
            return redirect(url_for('mostrar'))
    return render_template('nuevo.html')

if __name__ == "__main__":
    db.create_all()
    app.run()