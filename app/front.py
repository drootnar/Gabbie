import hashlib
from flask import Blueprint, render_template, redirect, jsonify
from flask.ext.login import login_user, current_user, logout_user, login_required
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from models.user import User
from sqlalchemy import and_
from app import db
from werkzeug.exceptions import BadRequest

front_blueprint = Blueprint('front', __name__)


@front_blueprint.route('')
def landing():
    return render_template('index.html')


@front_blueprint.route('login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(and_(
            User.username == form.username.data,
            User.password == hashlib.sha1(form.password.data).hexdigest()
        )).first()
        if user:
            login_user(user=user, remember=form.remember_me.data)
            return redirect('/panel')

    return render_template('login.html', form=form)


@front_blueprint.route('register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(None)
        user.username = form.username.data
        user.password = hashlib.sha1(form.password.data).hexdigest()
        db.session.add(user)
        try:
            db.session.commit()
            login_user(user)
            return redirect('/panel')
        except Exception as e:
            raise BadRequest()

    return render_template('register.html', form=form)


@front_blueprint.route('logout', methods=['GET'])
def logout():
    logout_user()
    return redirect('')


@front_blueprint.route('panel', methods=['GET'])
@login_required
def panel():
    return render_template('panel/index.html')

