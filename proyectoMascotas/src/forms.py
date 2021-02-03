from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, ValidationError
from src import tabla_solicitudes, tabla_mascotas

class SolicitudForm(FlaskForm):
    cedula = StringField('Cedula', validators=[
                           DataRequired(message='Ingrese su cedula porfavor porfavor')])
    nombre = StringField('Nombre', validators=[
                           DataRequired(message='Ingrese su nombre porfavor')])
    apellido = StringField('Apellido', validators=[
                           DataRequired(message='Ingrese su apellido porfavor')])
    correo = StringField('Email', validators=[DataRequired(
        message='Ingrese un email porfavor')])
    telefono = StringField('Número de teléfono', validators=[
                           DataRequired(message='Ingrese un número de telefono')])
    mascota = StringField('Mascota', validators=[
                           DataRequired(message='Ingrese la mascota que desea adoptar')])
    submit = SubmitField('Solicitar')
    def validar_solicitud(self, solicitud):
        mascota = tabla_solicitudes.find_one({'solicitud_id': solicitud.data})
        if not(solicitud):
            raise ValidationError(
                'No existe. Porfavor ingrese uno diferente')

class MascotaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
                           DataRequired(message='Ingrese el nombre porfavor')])
    edad = StringField('Edad', validators=[
                           DataRequired(message='Ingrese la edad porfavor')])
    animal = StringField('Animal', validators=[
                           DataRequired(message='Ingrese que animal es su mascota porfavor')])
    raza = StringField('Raza', validators=[
                           DataRequired(message='Ingrese la raza porfavor')])
    imagen = FileField('Foto')
    submit = SubmitField('Subir mascota')  

    def validar_mascota(self, codigo):
        mascota = tabla_mascotas.find_one({'codigo': codigo.data})
        if mascota:
            raise ValidationError(
                'Este codigo ya existe. Porfavor ingrese otro  codigo')