from flask import Blueprint, render_template

promod = Blueprint('profesional', __name__, template_folder='templates')

@promod.route('/profesional-index')
def profesionalIndex():
    return render_template('profesional-index.html')