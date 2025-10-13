from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore
import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import reserva
class Horario:
    def __init__(self, data):
            self.id = data['id']
            self.hora_inicio = data['hora_inicio']
            self.hora_fin = data['hora_fin']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
    @classmethod
    def get_by_name(cls, formulario):
        query= "DELETE FROM users WHERE name = %(name)s"
        result= connectToMySQL('esquema_maker').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            user = cls(result[0])
            return user