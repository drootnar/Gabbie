from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from front import front_blueprint
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from service import *

app.register_blueprint(front_blueprint, url_prefix='/')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


# All rooms
@app.route('/room', methods=['GET'])
def room_get():
    service = RoomService(db)
    data = {
        'major': request.args.get('major', None),
        'minor': request.args.get('minor', None),
    }
    rooms = service.get(data)
    return jsonify({
        'results': [room.__json__() for room in rooms],
    })


# Add room
@app.route('/room', methods=['POST'])
def room_post():
    service = RoomService(db)
    room = service.add(request.json)
    # return jsonify(room.__json__())
    return 'OK'

if __name__ == '__main__':
    app.run()
