from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class Contacto(Form):
    nombre = TextField("Nombre del Estudiante",[validators.Required("Por favor introduzca nombre...")])
    genero = RadioField("Genero", choices=[('M', 'Masculino'),('F','Femenino')])
    direccion = TextAreaField("Direccion")
    email = TextField("Correo",[validators.Required("Favor introduzca un correo..."), validators.Email("Favor introduzca un correo...")])
    edad = IntegerField("edad")
    lengprog = SelectField('Idioma', choices=[('py', 'Python'), ('js', 'JavaScript')])
    submit = SubmitField("Enviar")