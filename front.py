from flask import Blueprint

front_blueprint = Blueprint('front', __name__)


@front_blueprint.route('')
def landing():
    return 'landing'

