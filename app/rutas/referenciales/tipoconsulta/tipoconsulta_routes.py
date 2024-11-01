from flask import Blueprint, render_template

ipomod = Blueprint('tipoconsulta', __name__, template_folder='templates')

@ipomod.route('/tipoconsulta-index')
def tipoconsultaIndex():
    return render_template('tipoconsulta-index.html')