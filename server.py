from flask_app.__init__ import app
from flask_app.controllers import artists
from flask_app.controllers import albums
from flask import render_template

@app.route('/')
def index():
    return(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)