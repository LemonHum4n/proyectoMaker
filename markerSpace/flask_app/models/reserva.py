from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore

import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Reserva:
    def __init__(self, data):
            self.id = data['id']
            self.rut = data['rut']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.email = data['email']
            self.tipo_visita = data['tipo_visita']
            self.zone = data['zone']
            self.fecha_reserva = data['fecha_reserva']
            self.horario = data['horario']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

        
    @classmethod
    def save(cls, formulario):
        query = """
        INSERT INTO reserva 
        (rut, first_name, last_name, email, tipo_visita, zona, fecha_reserva, horario) 
        VALUES (%(rut)s, %(first_name)s, %(last_name)s, %(email)s, %(tipo_visita)s, %(zona)s, %(fecha_reserva)s, %(horario)s)
        """
        result = connectToMySQL('esquema_maker').query_db(query, formulario)
        return result

    @classmethod
    def exists(cls, fecha_reserva, horario, zone_id):
        query = """
        SELECT * FROM reserva 
        WHERE fecha_reserva = %(fecha_reserva)s AND horario = %(horario)s AND zone_id = %(zone_id)s
        """
        data = {
            "fecha_reserva": fecha_reserva,
            "horario": horario,
            "zone_id": zone_id
        }
        result = connectToMySQL('esquema_maker').query_db(query, data)
        return len(result) > 0

