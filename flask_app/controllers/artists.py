from flask import Flask, request, render_template, session, redirect
from flask_app.__init__ import app
from flask_app.models.artist import Artist

@app.route('/artists')
def all_artists():
    artists = Artist.get_all()
    return(render_template('artists.html', artists = artists))

# the following will need a post method/form in the appropriat template

@app.route('/update_artists', methods = ['POST'])
def artist_insertion():
    Artist.insertion(request.form['artist_name'], request.form['email'])
    return(redirect('/artists'))
