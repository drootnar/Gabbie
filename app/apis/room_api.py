from app.service import RoomService, RoomSchema
from flask import Blueprint, request, jsonify, abort
from app import db
from flask.ext.login import login_required, current_user
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
            'results': [room.json() for room in rooms],
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
@room_blueprint.route('/<room_id>', methods=['GET'])
def room_get_detail(room_id):
    service = RoomService(db)
    room = service.get_detail(room_id)
    if room:
        return jsonify(room.json())
    else:
        abort(404)


# Add message
@room_blueprint.route('/<room_id>/messages', methods=['POST'])
def add_message(room_id):
    service = RoomService(db)
    data = request.json
    data['room_id'] = room_id
    message = service.add_message(room_id, request.json)
    if message:
        return jsonify(message.json(verbose=True))
    else:
        abort(400)


# Add message
@room_blueprint.route('/<room_id>/messages_web', methods=['POST'])
@login_required
def add_message_web(room_id):
    service = RoomService(db)
    data = request.json
    data['room_id'] = room_id
    data['user_id'] = current_user.id
    message = service.add_message(room_id, request.json)
    if message:
        return jsonify(message.json(verbose=True))
    else:
        abort(400)


# Room messages
@room_blueprint.route('/<room_id>/messages', methods=['GET'])
def messages_list(room_id):
    service = RoomService(db)
    messages = service.list_messages(room_id, request.args)
    return jsonify({
        'results': [message.json() for message in messages],
    })


# Room messages detail
@room_blueprint.route('/<room_id>/messages/<message_id>', methods=['GET'])
def message_detail(room_id, message_id):
    service = RoomService(db)
    message = service.get_message(room_id, message_id)
    if message:
        return jsonify(message.json(verbose=True))
    else:
        abort(400)


# Room messages answer
@room_blueprint.route('/<room_id>/messages/<message_id>/answer', methods=['GET'])
def message_detail_answer(room_id, message_id):
    service = RoomService(db)
    message = service.answer_message(room_id, message_id)
    if message:
        return jsonify(message.json(verbose=True))
    else:
        abort(400)


# Room messages reject
@room_blueprint.route('/<room_id>/messages/<message_id>/reject', methods=['GET'])
def message_detail_reject(room_id, message_id):
    service = RoomService(db)
    message = service.reject_message(room_id, message_id)
    if message:
        return jsonify(message.json(verbose=True))
    else:
        abort(400)
