from PIL import Image
import os
import time
import secrets
from flask import render_template, flash, redirect, url_for, session, request, jsonify
from src import app, tabla_mascotas, tabla_solicitudes
from src.forms import BuscadorForm, SolicitudForm, MascotaForm
from bson.objectid import ObjectId

@app.route('/', methods =['GET', 'POST'])
def home():
    form = BuscadorForm()
    if form.validate_on_submit():
        solicitud = tabla_solicitudes.find_one({'solicitud_id': form.solicitud.data})
        if solicitud:
            session['solicitud_id'] = form.solicitud.data
            print(session['solicitud_id'])
            return redirect(url_for('buscar_solicitud'))
        flash('No existe la solicitud', 'warning')
    return render_template('buscador.html', form = form)

@app.route('/mascota', methods = ['GET', 'POST'])
def crear_mascota():
    form = MascotaForm()
    if form.validate_on_submit():
        picture_file, f_ext = save_picture(form.imagen.data)
        mascota = {
                    'nombre': form.nombre.data,
                    'edad': form.edad.data,
                    'animal': form.animal.data,
                    'raza': form.raza.data,
                    'imagen': picture_file
                    }
        tabla_mascotas.insert_one(mascota)
        form.nombre.data = ''
        form.edad.data = ''
        form.animal.data = ''
        form.raza.data = ''
        flash('Mascota subida satisfactoriamente', 'success')
    
    return render_template('mascota.html', form = form)

@app.route('/mascotas/<_id>/delete', methods=['POST'])
def borrar_mascota(_id):
    tabla_mascotas.delete_one({'_id': ObjectId(_id)})
    return redirect(url_for('ver_mascotas'))

@app.route('/solicitud', methods = ['GET', 'POST'])
def crear_solicitud():
    form = SolicitudForm()
    if form.validate_on_submit():
        solicitud = {
                    'cedula': form.cedula.data,
                    'nombre': form.nombre.data,
                    'apellido': form.apellido.data,
                    'correo': form.correo.data,
                    'telefono': form.telefono.data,
                    'mascota': form.mascota.data
                    }
        tabla_solicitudes.insert_one(solicitud)
        form.cedula.data = ''
        form.nombre.data = ''
        form.apellido.data = ''
        form.correo.data = ''
        form.telefono.data = ''
        form.mascota.data = ''
        flash('Solicitud enviada satisfactoriamente', 'success')
    return render_template('solicitud.html', form = form)

@app.route('/mascotas', methods = ['GET'])
def ver_mascotas():
    mascotas = tabla_mascotas.find_one({})
    if mascotas:
        mascotas = tabla_mascotas.find({})
        return render_template('mascotas.html', mascotas=mascotas)
    else: 
        return render_template('mascotas.html', vacio_mascotas = True)
    return render_template('mascotas.html', mascotas=mascotas)

@app.route('/ver/solicitudes', methods = ['GET'])
def ver_solicitudes():
    solicitudes = tabla_solicitudes.find_one({})
    if solicitudes:
        solicitudes = tabla_solicitudes.find({})
        return render_template('solicitudes.html', solicitudes=solicitudes)
    else: 
        return render_template('solicitudes.html', vacio_solicitudes = True)
    return render_template('solicitudes.html', solicitudes=solicitudes)

@app.route("/solicitudes/<_id>/delete", methods=['POST'])
def borrar_solicitud(_id):
    tabla_solicitudes.delete_one({'_id': ObjectId(_id)})
    return redirect(url_for('ver_solicitudes'))

def save_picture(form_picture):
    extensions = ['.jpg', '.jpeg', '.tif', '.png', '.PNG']
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    if f_ext in extensions:
        picture_path = os.path.join(
            app.root_path, 'static/Mascotas', picture_fn)
        output_size = (125, 125)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)

    return picture_fn, f_ext