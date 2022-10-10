
from ..config.mysqlconnection import connectToMySQL
class Artist:
    def __init__(self, data):
        self.id = data['id']
        self.artist_name = data['artist_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']
        self.albums = []
        self.labels = []
    @classmethod
    def insertion(cls, artist_name, email):
        query = "INSERT INTO music.artists (artist_name, email, created_at, updated_at) VALUES (%(artist_name)s,%(email)s,NOW(),NOW())"
        data = {'artist_name': artist_name,'email':email}    
        connectToMySQL('music').query_db(query,data)
    @classmethod
    def get_by(cls,condition):
        query = "SELECT * FROM artists WHERE artist_name LIKE %(condition)s OR email LIKE %(condition)s OR id = %(condition)s"
        data = {'condition': condition}
        results = connectToMySQL('music').query_db(query,data)
        artists = []
        for artist in results:
            artists.append(cls(artist))
        return(artists)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM music.artists;"
        results = connectToMySQL('music').query_db(query)
        artists = []
        for artist in results:
            artists.append(cls(artist))
        return(artists)
    @classmethod
    def delete_artist(cls, id):
        query = 'DELETE FROM artists WHERE id = %(id)s'
        data = {'id': id}
        connectToMySQL('music').query_db(query, data)
    @classmethod
    def albums_by(cls, id):
        query = 'SELECT title ,duration,format,date_issued,reissue_date,artists.artist_name FROM music.albums JOIN artists on artist_id = artists.id WHERE artist_id =%(id)s'
        data = {'id':id}
        albums = []
        result = connectToMySQL('music').query_db(query, data)
        for album in result:
            albums.append(album)
        return(albums)

