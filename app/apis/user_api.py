from app.service import UserService, UserSchema
from flask import Blueprint, request, jsonify
from app import db
from werkzeug.exceptions import BadRequest

user_blueprint = Blueprint('user_blueprint', __name__)


# All rooms
@user_blueprint.route('', methods=['GET'])
def user_get():
    service = UserService(db)
    data = {
        'major': request.args.get('major', None),
        'minor': request.args.get('minor', None),
    }
    users = service.get(data)
    return jsonify({
        'results': [user.json() for user in users],
    })


# Add room
@user_blueprint.route('', methods=['POST'])
def user_post():
    service = UserService(db)
    user = service.add(request.json)
    if user:
        return jsonify(user.json())
    else:
        raise BadRequest()
