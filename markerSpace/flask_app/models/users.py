from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #type: ignore

import re #Importando las expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.email = data['email']
            self.password = data['password']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']


    @staticmethod

    def valida_usuario(formulario):
        #formulario = DICCIONARIO con todos los names y values que el usuario ingresa
        es_valido = True 

        if len(formulario['first_name']) < 3:
            flash('Nombre debe tener al menos 3 caracteres', 'registro')
            es_valido = False

        if len(formulario['password']) < 6:
            flash('Contraseña debe tener al menos 6 caracteres', 'registro')
            es_valido = False

        if formulario['password'] != formulario['confirm_password']:
            flash('Contraseñas NO coinciden', 'registro')
            es_valido = False
        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail inválido', 'registro')
            es_valido = False
            
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_maker').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False
        else:
            flash('0', 'registro')
        
        
        return es_valido
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, email, password) VALUES (%(first_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_maker').query_db(query, formulario)
        return result 
    
    @classmethod
    def get_by_email(cls, formulario):
        query = "select * from users where email = %(email)s"
        result = connectToMySQL('esquema_maker').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            user = cls(result[0])
            return user
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('esquema_maker').query_db(query, data)
    