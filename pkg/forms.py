from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

class LoginForm(FlaskForm):
    matricula = StringField('Matrícula', validators=[DataRequired(message='*matrícula')])
    password = PasswordField('Password', validators=[DataRequired(message='*senha')])
    submit = SubmitField('Login')