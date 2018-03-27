from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///xxxx.db'
app.config['SECRET_KEY'] = 'wololo'

db = SQLAlchemy(app)

clase_estu = db.Table('clase_estu', 
                        db.Column('id_clase', db.Integer, db.ForeignKey('clases.id_clase')), 
                        db.Column('id_estudiante', db.Integer, db.ForeignKey('estudiantes.id_estudiante')))

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    id_estudiante = db.Column(db.Integer, primary_key=True)
    nombre_estudiante = db.Column(db.String(64))
    apellido_estudiante = db.Column(db.String(64))
    email_estudiante = db.Column(db.String(128))
    def __init__(self, n, a, e):
        self.nombre_estudiante = n
        self.apellido_estudiante = a
        self.email_estudiante = e

class Clase(db.Model):
    __tablename__ = 'clases'
    id_clase = db.Column(db.Integer, primary_key=True)
    nombre_clase = db.Column(db.String(128))
    relacion = db.relationship("Estudiante", secondary=clase_estu)
    def __init__(self, n):
        self.nombre_clase = n

@app.route('/')
def mostrar():
    return render_template('mostrar.html', estudiantes = Estudiante.query.all())

if __name__ == "__main__":
    db.create_all()
    e = Estudiante("Xenobia", "Petrov", "p4@p.com")
    c = Clase("Programacion")
    c.relacion.append(e)
    db.session.add(c)
    db.session.commit()
    app.run()

