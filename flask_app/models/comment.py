from  config.mysqlconnection import connectToMySQL

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.post_id = data['post_id']
        self.user_id = data['user_id']


    @classmethod
    def add_comment(cls, data):
        query = 'INSERT INTO comments (content, created_at,updated_at, user_id, post_id) VALUES (%(content)s, NOW(), NOW(),%(user_id)s,%(post_id)s)'
        connectToMySQL('music').query_db(query, data)
    