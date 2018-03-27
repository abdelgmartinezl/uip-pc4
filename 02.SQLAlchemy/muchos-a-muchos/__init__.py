from flask import Flask
from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clase11.db'
app.config['SECRET_KEY'] = 'wololo'

db = SQLAlchemy(app)

orden = db.Table('Orden', 
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')), 
    db.Column('producto_id', db.Integer, db.ForeignKey('producto.id')))

# class Orden(db.Model):
#     __tablename__ = 'orden'

#     id = db.Column(db.Integer, primary_key=True)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
#     producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(255))
    productos = db.relationship("Producto", secondary=orden)
    def __init__(self, c):
        self.correo = c

class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))

    def __init__(self, n):
        self.nombre = n

    #usuarios = relationship("Usuario", secondary="orden")

if __name__ == "__main__":
    db.create_all()

    #Generacion de datos
    u = Usuario(input("Usuario: "))
    p = Producto(input("Producto: "))   
    db.session.add(u)
    db.session.commit()
    db.session.add(p)
    db.session.commit()
    u.orden.append(p)
    db.session.commit()
    
    #Consulta de datos
    x1 = Usuario.query.first()
    x2 = Producto.query.first()
    x3 = Orden.query.first()

    print(x1)
    print(x2)
    print(x3)
    app.run()