from flask_app.__init__ import app
from flask_app.controllers import artists
from flask_app.controllers import albums
from flask import render_template
from flask_app.controllers import labels
from flask_app.controllers import users
from flask_app.controllers import posts
from flask_app.controllers import comments
@app.route('/')
def index():
    return(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)