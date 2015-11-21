from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(Form):
    username = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])