from flask import Flask, request, render_template, session, redirect
from flask_app.__init__ import app
from flask_app.models.album import Album
from flask_app.models.artist import Artist

#need some templates i.e. albumst.html etc with functionality
@app.route('/albums')
def get_all_albums():
    albums = Album.get_all_join()
    return(render_template('albums.html', albums = albums))
@app.route('/add_album', methods = ['POST'])
def add_album():
    data = request.form
    Album.insertion(data)
    return(redirect('/albums'))
@app.route('/albums_add', methods = ['GET'])
def swticheroo():
    return(redirect('/album_form'))
@app.route('/artist_albums/<id>')
def albumsByArtist(id):
    albums = Artist.albums_by(id)
    return(render_template('albums.html',albums = albums))
@app.route('/album_form', methods = ['GET','POST'])
def album_form():
    artists = Artist.get_all()
    # labels = Label.get_all()
    return(render_template('albums_add.html', artists = artists))
