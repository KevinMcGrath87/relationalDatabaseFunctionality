from flask_app.__init__ import app
from flask import render_template, redirect, session, flash, request
from flask_app.models import post


@app.route('/wall')
def load_wall():
    post_id = post.Post.get_last_id()
    # getalljoined now returns list of post objects with comment objects collected inside....
    posts = post.Post.get_all_joined()
    # post_id is still an int...posts is a collection of post objects user is the session....user
    return(render_template('wall.html', post_id = post_id, posts = posts, user = session['user']))

@app.route('/post_wall', methods = ['POST'])
def post_wall():
    data = request.form
    post.Post.make_post(data)
    return(redirect('/wall'))

