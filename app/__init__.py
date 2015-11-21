from flask import Flask, jsonify, request, render_template
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import os
from werkzeug.exceptions import HTTPException, BadRequest

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app.models.user import User

from front import front_blueprint
from apis.room_api import room_blueprint

app.register_blueprint(front_blueprint, url_prefix='/')
app.register_blueprint(room_blueprint, url_prefix='/api/v1/rooms')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(406)
@app.errorhandler(407)
@app.errorhandler(500)
@app.errorhandler(501)
@app.errorhandler(502)
def handle_this_shit(error):
    if 'api/v1' in request.url:
        if not isinstance(error, HTTPException):
            error = BadRequest()
        response = jsonify({'code': error.code, 'name': error.name, 'description': error.description})
        response.status_code = error.code
        return response
    else:
        return render_template('error.html', error=error)
