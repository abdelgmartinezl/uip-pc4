from flask import Flask
app = Flask(__name__)

@app.route('/')
def choteo():
    return 'Xopa moh!'

@app.route('/saludar')
def saludar():
    return 'Saludos cordiales!'

@app.route('/saludar/<nombre>')
def saludar_nombre(nombre):
    return 'Saludos, %s!' % nombre

@app.route('/calculadora/<int:a>')
def calcular_itbms(a):
    return str(a*1.07)

@app.route('/calculadora/<float:a>')
def calcular_itbms2(a):
    return str(a*1.07)

if __name__ == '__main__':
    app.run()