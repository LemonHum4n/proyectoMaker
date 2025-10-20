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

    @staticmethod
    def valida_horario(formulario):
        es_valido = True

        horario = formulario['horario']
        zona = formulario['zona']

        if zona == 'Impresion 3D':
            horas_disponibles = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
        elif zona == 'Corte Laser':
            horas_disponibles = ['10:30', '11:30', '12:30', '13:30', '14:30', '15:30', '16:30', '17:30']
        else:
            flash("Zona no valida.", "reserva")
            return False

        if horario not in horas_disponibles:
            flash(f"El horario seleccionado no está disponible para la zona {zona}.", "reserva")
            es_valido = False

        return es_valido
    
    @staticmethod
    def valida_fecha(formulario):
        es_valido = True

        fecha_reserva = formulario['fecha_reserva']

        query = """
        SELECT COUNT(*) AS total_reservas
        FROM reserva
        WHERE fecha_reserva = %(fecha_reserva)s;
        """
        resultado = connectToMySQL('esquema_maker').query_db(query, {'fecha_reserva': fecha_reserva})
        total_reservas = resultado[0]['total_reservas']

        if total_reservas >= 20:
            flash("La fecha seleccionada ya ha alcanzado el límite de reservas. Por favor, elija otra fecha.", "reserva")
            es_valido = False

        return es_valido
    
    @staticmethod
    def valida_zona(formulario):
        es_valido = True

        zona = formulario['zona']

        if zona not in ['Impresion 3D', 'Corte Laser']:
            flash("Zona no valida.", "reserva")
            es_valido = False

        return es_valido
    
    @staticmethod
    def valida_reserva(formulario):
        es_valido = True

        if not Reserva.valida_horario(formulario):
            es_valido = False

        if not Reserva.valida_fecha(formulario):
            es_valido = False

        if not Reserva.valida_zona(formulario):
            es_valido = False

        return es_valido
    
    