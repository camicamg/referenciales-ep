from flask import Blueprint, render_template

hormod = Blueprint('horario', __name__, template_folder='templates')

@hormod.route('/horario-index')
def horarioIndex():
    return render_template('horario-index.html')