import sys
sys.path.append("G:/codingdojo/python/flask_mysql/db_connection/records_env/flask_app")
from time import strftime
from config.mysqlconnection import connectToMySQL
from datetime import date, datetime


class Album:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.duration = data['duration']
        self.format =data['format']
        self.date_issued = data['date_issued']
        self.reissue_date = data['reissue_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.artist_id = data['artist_id']
        self.label_id = data['label_id']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM music.albums;"
        results = connectToMySQL('music').query_db(query)
        albums = []
        for album in results:
            albums.append(cls(album))
        return(albums)
#let data in the insertion method be a dictionary passing the formatted message sequence and request form values to the query
    @classmethod
    def insertion(cls, data):
        print(data['title'])
        query = "INSERT INTO music.albums (title, format, duration, date_issued, reissue_date, created_at,updated_at, artist_id, label_id) VALUES (%(title)s, %(format)s,%(duration)s,%(date_issued)s,%(reissue_date)s,NOW(),NOW(),%(artist_id)s,%(label_id)s)"
        connectToMySQL('music').query_db(query,data)
    @classmethod
    def get_all_join(cls):
        query = 'SELECT title ,duration,format,date_issued,reissue_date,artists.artist_name, labels.label_name FROM albums JOIN artists ON albums.artist_id= artists.id JOIN labels ON albums.label_id = labels.id;'
        results = connectToMySQL('music').query_db(query)
        albums = []
        for album in results:
            albums.append((album))
        print(albums)
        return(albums)
    @staticmethod
    def get_datetime():
        now = datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        return(now)
# get rid of this print statement at some point
print (Album.get_datetime())


