from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore

import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import user
from flask_app.models import horario
class Reserva:
    def __init__(self, data):
            self.id = data['id']
            self.user_id = data['user_id']
            self.rut = data['rut']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.email = data['email']
            self.tipo_visita = data['tipo_visita']
            self.zone_id = data['zone_id']
            self.fecha_reserva = data['fecha_reserva']
            self.horario_id = data['horario_id']
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
        
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (rut, first_name, last_name, email, tipo_visita, zone_id, fecha_reserva, horario_id) VALUES (%(rut)s, %(nombre)s, %(apellido)s, %(gmail)s, %(tipo_visita)s, %(zona)s, %(fecha)s, %(horario)s )"
        result = connectToMySQL('esquema_maker').query_db(query, formulario)
        return result 
    