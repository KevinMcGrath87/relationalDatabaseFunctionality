from flask_app.models import user
from flask_app.__init__ import app
from flask import render_template, redirect, session, flash, request

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
    data = request.form
    if data:
        if not user.User.validate_user(data, valtype ='new'):
        # I think the return is nested in inf statements...for validation.
            return(redirect('/new_form'))
        else:
            user.User.create_user(data)
            session['user'] = data
            return(redirect('/welcome'))
    else:
        return(redirect('new/form'))


@app.route('/login', methods = ['POST'])
def login():
    data = request.form
    test_user = user.User.get_user(data['email'])
    if test_user:
        print(data)
        if not user.User.validate_user(data,valtype='login'):
            return(redirect('/login_form'))
        else:
            session['user'] = test_user
            return((redirect('/welcome')))
    else:
        return(redirect('/login_form'))



@app.route('/welcome')
def welcome():
    return(render_template('login.html', name = session['user']['first_name']))

