from flask import Blueprint, render_template

abmmod = Blueprint('abm', __name__, template_folder='templates')

@abmmod.route('/abm-index')
def abmIndex():
    return render_template('abm-index.html')