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
    def datos(cls, zona):
        query = """
        SELECT tipo_visita, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM reserva WHERE zona = %(zona)s) AS porcentaje
        FROM reserva
        WHERE zona = %(zona)s
        GROUP BY tipo_visita;
        """
        resultados = connectToMySQL('esquema_maker').query_db(query, {'zona': zona})

        datos = [(resultado['tipo_visita'], resultado['porcentaje']) for resultado in resultados]
        return datos
    
    #-------
    @classmethod
    def existe_reserva(cls, zona, fecha_reserva, horario):
        query = """
        SELECT id FROM reserva
        WHERE zona = %(zona)s AND fecha_reserva = %(fecha_reserva)s AND horario = %(horario)s
        LIMIT 1;
        """
        params = {
            'zona': zona,
            'fecha_reserva': fecha_reserva,
            'horario': horario
        }
        resultado = connectToMySQL('esquema_maker').query_db(query, params)
        return True if resultado else False

    @classmethod
    def validar_horario(cls, formulario):
        """
        formulario debe contener 'zona', 'fecha_reserva' y 'horario'.
        Devuelve True si el horario está disponible, False si ya hay una reserva.
        """
        zona = formulario.get('zona')
        fecha = formulario.get('fecha_reserva')
        horario = formulario.get('horario')

        if not zona or not fecha or not horario:
            flash('Faltan datos para validar el horario.', 'reserva')
            return False

        if cls.existe_reserva(zona, fecha, horario):
            flash('El horario ya está reservado en esa fecha y zona.', 'reserva')
            return False

        return True