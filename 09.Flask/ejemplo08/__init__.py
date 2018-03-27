from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevo')
def nuevo_estudiante():
    return render_template('estudiante.html')

@app.route('/agregar', methods=["POST"])
def agregar_estudiante():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            direccion = request.form['direccion']
            ciudad = request.form['ciudad']
            pin = request.form['pin']
            with sql.connect("basedato.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO estudiantes(nombre, direccion, ciudad, pin) VALUES(?,?,?,?)", (nombre,direccion,ciudad,pin))
                conn.commit()
                mensaje = "Registro insertado exitosamente"
        except:
            conn.rollback()
            mensaje = "Error en la insercion de datos"
        finally:
            return render_template("resultado.html", mensaje=mensaje)
            conn.close()

@app.route('/listar')
def listar():
    conn = sql.connect("basedato.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM estudiantes")
    filas = cur.fetchall()
    return render_template("lista.html", filas=filas)

if __name__ == "__main__":
    app.run()