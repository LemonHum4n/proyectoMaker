from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore
import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import reserva
class Horario:
    def __init__(self, data):
            self.id = data['id']
            self.hora = data['hora']

    @staticmethod
    def validate_horario(horario):
        is_valida = True # asumimos que esto es true
        if len(horario['hora']) < 1:
            flash("El campo hora no puede estar vacio", "error_horario")
            is_valida = False
        return is_valida


    @classmethod
    def save(cls, data):
        query = "INSERT INTO horario (hora) VALUES (%(hora)s);"
        return connectToMySQL('esquema_maker').query_db(query, data)
    
    @staticmethod
    def get_all():
        query = "SELECT * FROM horario"
        results = connectToMySQL('esquema_maker').query_db(query)
        horarios = []
        for row in results:
            horarios.append(Horario(row))
        return horarios