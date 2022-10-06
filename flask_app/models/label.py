import sys
sys.path.append('g:/codingdojo/python/flask_mysql/db_connection/records_env/flask_app/config')
sys.path.append('g:/codingdojo/python/flask_mysql/db_connection/records_env/flask_app')
from models.album import Album
from flask_app.models.artist import Artist

from config.mysqlconnection import connectToMySQL

class Label:
    def __init__(self,data):
        self.id = data['id']
        self.label_name = data['label_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.artists = []
        self.albums = []
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM labels'
        result = connectToMySQL('music').query_db(query)
        labels = []
        for label in result:
            labels.append(cls(label))
        return(labels)

       # details = f'SELECT artist_name, title FROM labels LEFT JOIN albums ON labels.id = albums.label_id LEFT JOIN artists ON albums.artist_id = artists.id WHERE labels.id = {x['id']} 
    # must pass id dictionary in for data from the server route
    @classmethod
    def albums_by_label (cls, data):
        query = 'SELECT * FROM labels LEFT JOIN albums ON labels.id = albums.label_id LEFT JOIN artists ON albums.artist_id = artists.id WHERE labels.id = %(id)s'
        result = connectToMySQL('music').query_db(query, data)
        # I am hoing the label instance works despite being a join table....
        label = cls(result[0])
        for album in result:

            album_data = {
                'id' : album['albums.id'],
                'title' : album['title'],
                'format' : album['format'],
                'duration': album['duration'],
                'date_issued': album['date_issued'],
                'reissue_date': album['reissue_date'],
                'created_at': album['albums.created_at'],
                'updated_at': album['albums.created_at'],
                'artist_id': album['artist_id'],
                'label_id': album['label_id']
            }
            label.albums.append(Album(album_data))
        # should return a label object with the albums inside
        return(label.albums)


    @classmethod
    def artists_by_label (cls, data):
        query = 'SELECT * FROM labels LEFT JOIN albums ON labels.id = albums.label_id LEFT JOIN artists ON albums.artist_id = artists.id WHERE labels.id = %(id)s'
        result = connectToMySQL('music').query_db(query, data)
        # I am hoing the label instance works despite being a join table....
        label = cls(result[0])
        for artist in result:
            artist_data = {
                'id' : artist['artists.id'],
                'artist_name' : artist['artist_name'],
                'email' : artist['email'],
                'created_at': artist['artists.created_at'],
                'updated_at': artist['artists.updated_at'],
            }
            label.artists.append(Artist(artist_data))
        # should return a label object with the albums inside
        return(label.artists)
