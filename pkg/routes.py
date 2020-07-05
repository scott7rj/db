import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from pkg import app, bcrypt
from pkg.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required

from usuariopkg.usuario_facade import UsuarioFacade
from usuariopkg.usuario import Usuario
from menupkg.menu1_facade import Menu1Facade
from menupkg.menu1 import Menu1
from menupkg.menu_builder import MenuBuilder

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    #form = LoginForm()
    #if form.validate_on_submit():
    #    usuario = Usuario()
    #    facade = UsuarioFacade()
    #    usuario = facade.get_user_by_matricula(form.matricula.data)
    #    if usuario and bcrypt.check_password_hash(usuario.senha, form.password.data):
    #        login_user(usuario, remember=form.remember.data)
    #        next_page = request.args.get('next')
    #        return redirect(next_page) if next_page else redirect(url_for('home'))
    #    print('ok')
    #else:
    #    flash('Login unsuccesful. Please check matricula and password', 'danger')
    return render_template('index.html', title='Index')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    print('Menu')
    print(request.form.get('txtId'))
    print(request.form.get('txtPwd'))
    usuario = Usuario()
    usuario_facade = UsuarioFacade()
    result = usuario_facade.get_user_by_matricula(str(request.form.get('txtId')).upper())
    usuario = usuario_facade.to_usuario()
    if result.rowcount == 1 and bcrypt.check_password_hash(usuario.senha, request.form.get('txtPwd')):
        print('User OK!')
        menu_builder = MenuBuilder()
        menu = menu_builder.build(usuario.perfil)
    else:
        print('Bad User!')
        return """§999§Bad User!"""
    return menu