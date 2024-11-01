from flask import Blueprint, render_template

tipmod = Blueprint('tipolesion', __name__, template_folder='templates')

@tipmod.route('/tipolesion-index')
def tipolesionIndex():
    return render_template('tipolesion-index.html')