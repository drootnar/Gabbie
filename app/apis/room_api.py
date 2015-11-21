from app.service import RoomService, RoomSchema
from flask import Blueprint, request, jsonify
from app import db
from werkzeug.exceptions import BadRequest

room_blueprint = Blueprint('room_blueprint', __name__)


# All rooms
@room_blueprint.route('', methods=['GET'])
def room_get():
    service = RoomService(db)
    data = {
        'major': request.args.get('major', None),
        'minor': request.args.get('minor', None),
    }
    rooms = service.get(data)
    return jsonify({
        'results': RoomSchema(many=True).dump(rooms).data,
    })


# Add room
@room_blueprint.route('', methods=['POST'])
def room_post():
    service = RoomService(db)
    room = service.add(request.json)
    if room:
        return jsonify(RoomSchema().dump(room).data)
    else:
        raise BadRequest()
