from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, ValidationError
from src import tabla_carritos, tabla_productos

class BuscadorForm(FlaskForm):
    mascota = StringField('Animales', validators=[
                           DataRequired(message='Ingrese un animal que desee buscar')])
    submit = SubmitField('Consultar')
    
    def validar_carrito(self, mascota):
        mascota = tabla_carritos.find_one({'carrito_id': mascota.data})
        if not(mascota):
            raise ValidationError(
                'No existe. Porfavor ingrese uno diferente')


class PagoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
                           DataRequired(message='Ingrese su nombre porfavor')])
    apellido = StringField('Apellido', validators=[
                           DataRequired(message='Ingrese su apellido porfavor')])
    cedula = StringField('Cedula', validators=[
                           DataRequired(message='Ingrese su cedula porfavor porfavor')])
    email = StringField('Email', validators=[DataRequired(
        message='Ingrese un email porfavor')])
    telefono = StringField('Número de teléfono', validators=[
                           DataRequired(message='Ingrese un número de telefono')])
    submit = SubmitField('Solicitar')

class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
                           DataRequired(message='Ingrese el nombre porfavor')])
    edad = StringField('Edad', validators=[
                           DataRequired(message='Ingrese la edad porfavor')])
    animal = StringField('Animal', validators=[
                           DataRequired(message='Ingrese que animal es su mascota porfavor')])
    raza = IntegerField('Raza', validators=[
                           DataRequired(message='Ingrese la raza porfavor')])
    imagen = FileField('Foto')
    submit = SubmitField('Subir mascota')  

    def validar_producto(self, codigo):
        producto = tabla_productos.find_one({'codigo': codigo.data})
        if producto:
            raise ValidationError(
                'Este codigo ya existe. Porfavor ingrese otro  codigo')