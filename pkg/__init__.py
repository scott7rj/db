import os
from flask import Flask
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '3aa920f302755adc709b6e51c7ffbaf7'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login' #function name of route
#login_manager.login_message = 'Matrícula ou senha inválidos. Verifique.'
#login_manager.login_message_category = 'info'

from pkg import routes