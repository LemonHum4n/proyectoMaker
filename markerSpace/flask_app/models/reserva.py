from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore

import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
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
            self.horario = data['horario']
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
        query = """
        INSERT INTO reserva 
        (user_id, rut, first_name, last_name, email, tipo_visita, zone_id, fecha_reserva, horario) 
        VALUES (%(user_id)s, %(rut)s, %(first_name)s, %(last_name)s, %(email)s, %(tipo_visita)s, %(zone_id)s, %(fecha_reserva)s, %(horario)s)
        """
        result = connectToMySQL('esquema_maker').query_db(query, formulario)
        return result
