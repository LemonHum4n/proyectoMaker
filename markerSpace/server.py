#0.- Una vez en el sistema --> pip install pipenv en cmd como administrador
#1.- Instalar flask, pymysql y bcrypt ->pipenv install flask pymysql flask-bcrypt en vs
#2.- pipenv shell -> py -m pipenv shell, python -m pipenv shell   en vs, activa el ambiente virtual
#3.- python nombre_archivo.py -> python3 nombre_archivo.py, py nombre_archivo.py    en vs

from flask_app import app
from flask_app.controllers import users_controller

#hola hola tilines

# holaa

# aaaaaaa

if __name__=="__main__":
    app.run(debug=True)