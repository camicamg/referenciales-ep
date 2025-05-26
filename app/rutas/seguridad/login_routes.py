from flask import Blueprint, render_template, session, \
    request, redirect, url_for, flash, current_app as app
from werkzeug.security import check_password_hash
from app.dao.referenciales.usuario.login_dao import LoginDao

logmod = Blueprint('login', __name__, template_folder='templates')

@logmod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # lo que viene del formulario
        usuario_nombre = request.form['usuario_nombre']
        usuario_clave = request.form['usuario_clave']
        # hacer la validacion contra la bd
        login_dao = LoginDao()
        usuario_encontrado = login_dao.buscarUsuario(usuario_nombre)
        if usuario_encontrado and 'usu_nick' in usuario_encontrado:
            password_hash_del_usuario = usuario_encontrado['usu_clave']
            print("password_hash_del_usuario:", password_hash_del_usuario)
            #TODO: VER  LOGIN VALIDO DESPUES
            #if check_password_hash(
            #   pwhash=password_hash_del_usuario, password=usuario_clave):
            print(f"evaluacion!! {password_hash_del_usuario} {usuario_clave}")
            if password_hash_del_usuario == usuario_clave:
                # crear la sesión
                session.clear() # limpiar cualquier sesión previa
                session.permanent = True
                session['usu_id'] = usuario_encontrado['usu_id']
                session['usu_nick'] = request.form['usuario_nombre']
                session['usuario_nombre'] = request.form['usu_nick']
                #session['usuario_nombre'] = request.form['usuario_nombre']
                #session['nombre_persona'] = usuario_encontrado['nombre_persona']
                #session['grupo'] = usuario_encontrado['grupo']
                print("antes de redirect!!!!!!!!")
                return redirect(url_for('login.inicio'))
        else:
            flash('Error de log in, no existe este usuario', 'warning')
            return redirect(url_for('login.login'))
    elif request.method == 'GET':
        print('request.method == get!!!!!!!!!!!!!')
        return render_template('inicio.html')

@logmod.route('/logout')
def logout():
    session.clear() # limpiar cualquier sesión previa
    flash('Sesion cerrada', 'warning')
    return redirect(url_for('login.login'))

@logmod.route('/')
def inicio():
    print('inicio!!', session)
    if 'usuario_nombre' in session:
        return render_template('inicio.html')
    else:
        return redirect(url_for('login.login'))