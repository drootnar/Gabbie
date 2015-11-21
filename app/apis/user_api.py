from app.service import UserService, UserSchema
from flask import Blueprint, request, jsonify
from app import db
from werkzeug.exceptions import BadRequest

user_blueprint = Blueprint('user_blueprint', __name__)


# All users
@user_blueprint.route('', methods=['GET'])
def user_get():
    service = UserService(db)
    users = service.get(data)
    return jsonify({
        'results': [user.json() for user in users],
    })


# Add user - mobile
@user_blueprint.route('', methods=['POST'])
def user_post():
    service = UserService(db)
    user = service.add(request.json)
    if user:
        return jsonify(user.json())
    else:
        raise BadRequest()
