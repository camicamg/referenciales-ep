from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.cargo.cargo_routes import carmod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.turno.turno_routes import turmod
from app.rutas.referenciales.sexo.sexo_routes import sexmod
from app.rutas.referenciales.dia.dia_routes import diamod
from app.rutas.referenciales.sucursal.sucursal_routes import sucmod
from app.rutas.referenciales.horario.horario_routes import hormod


# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(carmod, url_prefix=f'{modulo0}/cargo')
app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')
app.register_blueprint(sexmod, url_prefix=f'{modulo0}/sexo')
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia')
app.register_blueprint(sucmod, url_prefix=f'{modulo0}/sucursal')
app.register_blueprint(hormod, url_prefix=f'{modulo0}/horario')



from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.cargo.cargo_api import carapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.persona.persona_api import perapi
from app.rutas.referenciales.turno.turno_api import turapi
from app.rutas.referenciales.sexo.sexo_api import sexapi
from app.rutas.referenciales.dia.dia_api import diaapi
from app.rutas.referenciales.sucursal.sucursal_api import sucapi
from app.rutas.referenciales.horario.horario_api import horapi



# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(carapi, url_prefix=version1)
app.register_blueprint(nacapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(perapi, url_prefix=version1)
app.register_blueprint(turapi, url_prefix=version1)
app.register_blueprint(sexapi, url_prefix=version1)
app.register_blueprint(diaapi, url_prefix=version1)
app.register_blueprint(sucapi, url_prefix=version1)
app.register_blueprint(horapi, url_prefix=version1)