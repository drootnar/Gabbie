from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from front import front_blueprint
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

app.register_blueprint(front_blueprint, url_prefix='/')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
