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
    
    # aqui los metodos para validar horas , fechas y zonas

    @classmethod
    def validar_disponibilidad(cls, formulario):
        query = """
        SELECT COUNT(*) AS cantidad
        FROM reserva
        WHERE zona = %(zona)s AND fecha_reserva = %(fecha_reserva)s AND horario = %(horario)s;
        """
        resultado = connectToMySQL('esquema_maker').query_db(query, formulario)
        return resultado[0]['cantidad'] == 0  # Retorna True si no hay reservas, False si ya existe una reserva
    
    @staticmethod
    def valida_reserva(formulario):
        es_valido = True 

        if len(formulario['first_name']) < 2:
            flash('Nombre debe tener al menos 2 caracteres', 'reserva')
            es_valido = False

        if len(formulario['last_name']) < 2:
            flash('Apellido debe tener al menos 2 caracteres', 'reserva')
            es_valido = False

        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail inválido', 'reserva')
            es_valido = False

        # Validar disponibilidad
        if not Reserva.validar_disponibilidad(formulario):
            flash('La zona, fecha y horario seleccionados ya están reservados. Por favor, elija otra opción.', 'reserva')
            es_valido = False

        return es_valido