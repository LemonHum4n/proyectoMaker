from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore
import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# from flask_app.models import user
# from flask_app.models import reserva
class Horario:
    def __init__(self, data):
            self.id = data['id']
            self.hora = data['hora']

    @staticmethod
    def valida_horario(horario):
        is_valid = True 
        if len(horario['hora']) < 1:
            flash("El campo hora es obligatorio", 'horario')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO horarios (hora) VALUES (%(hora)s);"
        result = connectToMySQL('esquema_maker').query_db(query, formulario)
        return result
    