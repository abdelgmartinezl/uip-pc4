from flask import Flask, render_template, request, flash
from formas import Contacto

app = Flask(__name__)
app.secret_key = 'wololo'

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    forma = Contacto()
    if request.method == 'POST':
        if forma.validate() == False:
            flash("Todos los campos son requeridos.")
            return render_template('contacto.html', form=forma)
        else:
            return render_template('exito.html')
    elif request.method == 'GET':
        return render_template('contacto.html', form=forma)

if __name__ == "__main__":
    app.run()