from flask import render_template, redirect, request, session, flash #type: ignore
from flask_app import app

from flask_app.models.users import User

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

@app.route('/eliminar_reserva', methods=['POST'])
def eliminar_reserva():
    return render_template('registro.html')

@app.route('/logro')
def logro():
    return render_template('reserva.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/estadisticas')
def estadisticas():
    datos = [
        ('Administrador', 45),
        ('Usuario', 30),
        ('Invitado', 25)
    ]
    return render_template('estadistica.html', estadisticas=datos)

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

    return render_template('resitro.html')


@app.route('/reserva', methods=['POST'])
def mostrar_reserva():
    formulario_reserva = {
        "user_id": session.get('user_id'),
        "rut": request.form.get('rut'),
        "first_name": request.form.get('nombre'),
        "last_name": request.form.get('apellido'),
        "email": request.form.get('gmail'),
        "tipo_visita": request.form.get('tipo_visita'),
        "zone_id": request.form.get('zona'),
        "fecha_reserva": request.form.get('fecha'),
        "horario_id": request.form.get('horario')
    }

    # Guardar la reserva en la base de datos
    from flask_app.models.reserva import Reserva
    Reserva.save(formulario_reserva)

    flash('Reserva realizada con éxito', 'reserva')
    return redirect('/reserva')