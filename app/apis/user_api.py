from app.service import UserService
from flask import Blueprint, request, jsonify, abort
from app import db
from werkzeug.exceptions import BadRequest

user_blueprint = Blueprint('user_blueprint', __name__)


# All users
@user_blueprint.route('', methods=['GET'])
def user_get_all():
    service = UserService(db)
    users = service.get_all()
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


# Get user detail
@user_blueprint.route('/<user_id>', methods=['GET'])
def user_get(user_id):
    service = UserService(db)
    user = service.get(user_id)
    if user:
        return jsonify(user.json(verbose=True))
    else:
        abort(404)
