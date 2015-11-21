from app.service import RoomService, RoomSchema
from flask import Blueprint, request, jsonify, abort
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
    if rooms.count() == 1L:
        return jsonify(rooms[0].json())
    else:
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


# Room detail
@room_blueprint.route('<room_id>', methods=['GET'])
def room_get_detail(room_id):
    service = RoomService(db)
    room = service.get_detail(room_id)
    if room:
        return jsonify(room.json())
    else:
        abort(404)
