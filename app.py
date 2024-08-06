from flask import Flask, request, render_template as rt , redirect , url_for
from model import * 
from apis import *
from routs import router
import os
from flask_restful import Api


current_dir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ os.path.join(current_dir,"mad-1.sqlite3")
app.jinja_options = app.jinja_options.copy()
app.jinja_options['variable_start_string'] = '[['
app.jinja_options['variable_end_string'] = ']]'



db.init_app(app)
app.app_context().push()

api = Api(app)

api.add_resource(playList ,'/api/playlist' )
api.add_resource(testAPI, '/api/test' , '/api/test/<i>' )
api.add_resource(api_songs, '/api/songs/<tag>/<searchQuery>'  )

router(app)



@app.route('/vue')
def vue():
    return rt('vue.html')

if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')


