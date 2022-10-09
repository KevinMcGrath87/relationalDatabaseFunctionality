from flask_app.models import user
from flask_app.__init__ import app
from flask import render_template, redirect, session, flash, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#need some templates i.e. albumst.html etc with functionality
@app.route('/users')
def users_page():
    return(render_template('users.html'))

@app.route('/new_form')
def new_form():
    return(render_template('create_new_user.html'))

@app.route('/login_form')
def login_form():
    return(render_template('login_user_account.html'))


# will need to add validation for this route
@app.route('/add_user', methods = ['POST'])
def add_user():
    data = request.form.to_dict()
    if data:
        if not user.User.validate_user(data, valtype ='new'):
            return(redirect('/new_form'))
        else:
            pw_hash = bcrypt.generate_password_hash(data['user_password'])
            data['user_password']= pw_hash
            new_user = user.User.create_user(data)
            session['user'] = user.User.get_user_by_id(new_user)
            return(redirect('/welcome'))
    else:
        return(redirect('new/form'))


@app.route('/login', methods = ['POST'])
def login():
    data = request.form
    test_user = user.User.get_user(data['email'])
    if test_user:
        if not bcrypt.check_password_hash(test_user['user_password'], data['user_password']):
            flash('password does not match user')
            return(redirect('/login_form'))
        elif not user.User.validate_user(data,valtype='login'):
            return(redirect('/login_form'))
        else:
            session['user'] = test_user
            return((redirect('/welcome')))
    else:
        user.User.validate_user(data,valtype='login')
        return(redirect('/login_form'))


@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return(redirect('/users'))

@app.route('/welcome')
def welcome():
    if 'user' in session:
        return(render_template('login.html', name = session['user']['first_name']))
    else:
        flash('user has yet to log in')
        return(redirect('/users'))

