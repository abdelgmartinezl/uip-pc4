from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'uippc4@gmail.com'
app.config['MAIL_PASSWORD'] = '1qaz2wsxC.'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    mensaje = Message('Holi', sender='uippc4@gmail.com', 
                recipients=['uippc4@gmail.com'])
    mensaje.subject = "Asunto pue!"
    mensaje.body = "Chotiando desde Flask"
    mail.send(mensaje)
    return "Enviado"

if __name__ == "__main__":
    app.run()