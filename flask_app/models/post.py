from flask_app.models import comment
from  config.mysqlconnection import connectToMySQL

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.rank = data['rank']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.comments = []
    @staticmethod
    def get_last_id():
        query = 'SELECT * FROM posts'
        postlist = connectToMySQL('music').query_db(query)
        if postlist:
            length = len(postlist)
            last_id = postlist[length-1]['id']
            return(last_id)
        else:
            return(0)
    @classmethod
    def get_post_by(cls,id):
        query = 'SELECT * FROM posts where id = %(id)s'
        id = {'id': id}
        result = connectToMySQL('music').query_db(query, id)
        return result[0]

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM posts'
        postlist = connectToMySQL('music').query_db(query)
        if postlist:
            return(postlist)
        else:
            return(0)
# collecting lists of objects instead of dictionaries.
    @classmethod
    def get_all_joined(cls):
        query = 'SELECT * FROM posts LEFT JOIN users ON user_id = users.id LEFT JOIN comments ON posts.id = comments.post_id'
        postlist = connectToMySQL('music').query_db(query)
        postcollect = []
        for post in postlist:
            collector = cls(post)
            subquery = 'SELECT * FROM comments where post_id = %(id)s'
            subdict = {'id':collector.id}
            collection = connectToMySQL('music').query_db(subquery,subdict)
            for com in collection:
                com = comment.Comment(com)
                collector.comments.append(com)
            postcollect.append(collector)
        return(postcollect)


    @classmethod
    def make_post(cls, data):
        query = 'INSERT INTO posts (content, created_at,updated_at, user_id) VALUES (%(content)s, NOW(), NOW(),%(user_id)s)'
        print(data)
        id = connectToMySQL('music').query_db(query, data)
        post = (cls.get_post_by(id))
        return(post)






