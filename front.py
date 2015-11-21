from flask import Blueprint, render_template

front_blueprint = Blueprint('front', __name__)


@front_blueprint.route('')
def landing():
    return render_template('index.html')


@front_blueprint.route('login')
def login():
    return render_template('login.html')