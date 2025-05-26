from datetime import timedelta
from flask import Flask

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# creamos el token
csrf = CSRFProtect()
csrf.init_app(app)

# inicializar el secret key
app.secret_key = b'_5#y2L"F6Q7z\n\xec]/'

# Establecer duración de la sesión, 15 minutos
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

# importar modulo de seguridad
from app.rutas.seguridad.login_routes import logmod
app.register_blueprint(logmod)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.persona.persona_routes import persmod
from app.rutas.referenciales.dia.dia_routes import diamod
from app.rutas.referenciales.horario.horario_routes import hormod
from app.rutas.referenciales.departamento.departamento_routes import depmod

#importar abm
from app.rutas.abm.abm_routes import abmmod




# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(persmod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia')
app.register_blueprint(hormod, url_prefix=f'{modulo0}/horario')
app.register_blueprint(depmod, url_prefix=f'{modulo0}/departamento')

#registrar abm
modulo1 = '/abm'
app.register_blueprint(abmmod, url_prefix=f'{modulo1}/abm')




from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.persona.persona_api import persapi
from app.rutas.referenciales.dia.dia_api import diaapi
from app.rutas.referenciales.horario.horario_api import horapi
from app.rutas.referenciales.departamento.departamento_api import depapi




# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(nacapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(persapi, url_prefix=version1)
app.register_blueprint(diaapi, url_prefix=version1)
app.register_blueprint(horapi, url_prefix=version1)
app.register_blueprint(depapi, url_prefix=version1)


