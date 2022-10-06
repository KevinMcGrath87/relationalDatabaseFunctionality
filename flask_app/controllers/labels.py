from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY
from flask import Flask, request, redirect, render_template, session
from models.label import Label
from flask_app.__init__ import app

@app.route('/labels')
def get_all():
    labels = Label.get_all()
    return(render_template('labels.html', labels = labels))

@app.route('/label_albums/<id>')
def get_albums(id):
    albums = Label.albums_by_label({'id':id})
    print(albums)
    return(render_template('albums.html', albums = albums))

@app.route('/label_artists/<id>', methods = ['GET','POST'])
def get_artists(id):
    artists = Label.artists_by_label({'id':id})
    return(render_template('artists.html', artists = artists))
