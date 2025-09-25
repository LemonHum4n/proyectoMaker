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
        "last_name": request.form['last_name'],
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

@app.route('/logro')
def logro():
    return render_template('inicio_sesion.html')




    
