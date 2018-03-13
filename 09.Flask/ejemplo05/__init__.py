from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/subir')
def subir_archivo():
    return render_template('subir.html')

@app.route('/estibador', methods=['GET', 'POST'])
def estibar():
    if request.method == 'POST':
        archivo = request.files['archivo']
        archivo.save("/tmp/"+secure_filename(archivo.filename))
        return 'Archivo subido exitosamente'

if __name__ == '__main__':
    app.run()