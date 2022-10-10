from flask_app.__init__ import app
from flask import render_template, redirect, session, flash, request
from flask_app.models import comment

@app.route('/comment', methods = ['POST'])
def make_comment():
    comment.Comment.add_comment(request.form)
    return(redirect('/wall'))