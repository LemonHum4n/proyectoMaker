from flask import render_template, redirect, request, session, flash #type: ignore
from flask_app import app

from flask_app.models.users import User
from flask_app.models.reserva import Reserva

from flask_bcrypt import Bcrypt #type: ignore

bcrypt=Bcrypt(app)




@app.route('/')
def index():
    return render_template('registro.html')

@app.route('/register', methods=['POST'])
def register ():
    if not User.valida_usuario(request.form):
        return redirect('/')
    
    pwd=bcrypt.generate_password_hash(request.form['password'])

    formulario = {
        "first_name": request.form['first_name'],
        "email": request.form['email'],
        "password": pwd
    }
    
    id = User.save(formulario)

    session['user_id'] = id
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash('Correo no encontrado', 'inicio_sesion')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Contraseña incorrecta', 'inicio_sesion')
        return redirect('/')
        
    
    
    session['user_id'] = user.id
    return redirect('/logro')

@app.route('/eliminar_cuenta', methods=['POST'])
def eliminar_cuenta():
    return render_template('registro.html')

@app.route('/eliminar_reserva')
def eliminar_reserva():
    return render_template('delete_reserve.html')

@app.route('/logro')
def logro():
    return render_template('reserva.html')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        formulario = {
            'rut': request.form['rut'],
            'first_name': request.form['nombre'],
            'last_name': request.form['apellido'],
            'email': request.form['gmail'],
            'tipo_visita': request.form['tipo_visita'],
            'zona': request.form['zona'],
            'fecha_reserva': request.form['fecha'],
            'horario': request.form['horario']
        }
        Reserva.save(formulario)
        return redirect('/reserva')
    return render_template('reserva.html')

@app.route('/estadisticas')
def estadisticas():
    zonas = ['Impresora 3D', 'Router CNC', 'Cortadora laser', 'Clase capacitacion', 'Sala de clases', 'Taller', 'Domo de batalla robotica']
    datos_por_zona = {}

    for zona in zonas:
        datos_por_zona[zona] = Reserva.datos(zona)

    return render_template('estadistica.html', datos_por_zona=datos_por_zona)

@app.route('/delete', methods=['POST'])
def delete():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.get_by_email({'email': email})

    if user and bcrypt.check_password_hash(user.password, password):
        deleted = User.delete({'id': user.id})
        if deleted:
            session.clear()
            flash('0', category='delete_account')
        else:
            flash('Error al eliminar la cuenta.', category='delete_account')
    else:
        flash('Email o contraseña incorrectos.', category='delete_account')

    return render_template('registro.html')

@app.route('/delete_reserve', methods=['POST'])
def delete_reserve():
    first_name = request.form.get('first_name')
    password = request.form.get('password')
    user = User.get_by_email({'first_name': first_name})
    if user and bcrypt.check_password_hash(user.password, password):
        deleted = User.delete({'id': user.id})
        if deleted:
            session.clear()
            flash('0', category='delete_account')
        else:
            flash('Error al eliminar la cuenta.', category='delete_account')
    else:
        flash('Nombre o contraseña incorrectos.', category='delete_account')

    return render_template('registro.html')

@app.route('/reserva_guardar', methods=['POST'])
def guardar_reserva():
    formulario = {
        'rut': request.form['rut'],
        'first_name': request.form['nombre'],
        'last_name': request.form['apellido'],
        'email': request.form['gmail'],
        'tipo_visita': request.form['tipo_visita'],
        'zona': request.form['zona'],
        'fecha_reserva': request.form['fecha'],
        'horario': request.form['horario']
    }
    Reserva.save(formulario)
    return redirect('/reserva')





