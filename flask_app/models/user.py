from flask import flash
from ..config.mysqlconnection import connectToMySQL
import re
REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')




class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.user_password = data['user_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        result = connectToMySQL('music').query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return(users)
# next method must be passed ... form content to created instance of user i.e. dictionary of values from fomr into data
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, user_password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(user_password)s, NOW(), NOW())'
        result = connectToMySQL('music').query_db(query,data)
        # returns the id of the user. 
        return(result)
    @classmethod
    def get_user(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        data = {'email':data}
        user = connectToMySQL('music').query_db(query, data)
        if user:
            return(user[0])
        else:
            return(False)

    @staticmethod
    def validate_user(data, valtype):
        this_user =  User.get_user(data['email'])
        userlist = User.get_all()
        is_valid = True
        for key in data:
            if not len(str(data[key])) > 0:
                flash('no fields can be left blank', 'error1')
                is_valid = False
                break
        if valtype == 'new':
            if len(data['first_name']) < 5:
                flash('first name must be at least 5 characters')
                is_valid = False
            if len(data['last_name'])< 5:
                flash ('last name must be at least 5 characters')
                is_valid = False
            # this portion requires regex matching///placeholder for now
            if not REGEX_EMAIL.match(data['email']):
                flash ('invalid email format')
                is_valid = False
            for users in userlist:
                if data['email'] == users.email:
                    flash('email must be unique')
                    is_valid = False
                    break
            if len(data['user_password']) < 5:
                flash("password must be at least 5 characters")
            # this executes if getuser returns and existing user to the database
        else:
            if this_user:
                print(this_user['user_password'])
                print(data['user_password'])
                if not re.match(data['user_password'], this_user['user_password'] ):
                    flash('user exists: password does not match stored password')
                    is_valid = False
                if not re.match(data['email'],this_user['email']):
                    flash('user exists: email does not match account')
                    is_valid = False
        return(is_valid)