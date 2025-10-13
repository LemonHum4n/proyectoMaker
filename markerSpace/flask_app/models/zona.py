from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #type: ignore
import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# from flask_app.models import reserva
# from flask_app.models import user
class Zona:
    def __init__(self, data):
            self.id = data['id']
            self.nombre = data['nombre']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

    @staticmethod
    def valida_zona(zona):
        is_valida = True 
        if len(zona['nombre']) < 1:
            flash("El campo nombre es obligatorio", 'zona')
            is_valida = False
        return is_valida
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM zonas;"
        results = connectToMySQL('esquema_maker').query_db(query)
        zonas = []
        for zona in results:
            zonas.append( cls(zona) )
        return zonas