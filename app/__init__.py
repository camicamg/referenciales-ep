from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.cargo.cargo_routes import carmod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.turno.turno_routes import turmod
from app.rutas.referenciales.dia.dia_routes import diamod
from app.rutas.referenciales.sucursal.sucursal_routes import sucmod
from app.rutas.referenciales.horario.horario_routes import hormod
from app.rutas.referenciales.tipolesion.tipolesion_routes import tipmod
from app.rutas.referenciales.tipoconsulta.tipoconsulta_routes import ipomod
from app.rutas.referenciales.profesional.profesional_routes import promod
from app.rutas.referenciales.departamento.departamento_routes import depmod


# importar gestionar compras
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedidos_compras_routes \
    import pdcmod



# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(carmod, url_prefix=f'{modulo0}/cargo')
app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia')
app.register_blueprint(sucmod, url_prefix=f'{modulo0}/sucursal')
app.register_blueprint(hormod, url_prefix=f'{modulo0}/horario')
app.register_blueprint(tipmod, url_prefix=f'{modulo0}/tipolesion')
app.register_blueprint(ipomod, url_prefix=f'{modulo0}/tipoconsulta')
app.register_blueprint(promod, url_prefix=f'{modulo0}/profesional')
app.register_blueprint(depmod, url_prefix=f'{modulo0}/departamento')


# registro de modulos - gestionar compras
modulo1 = '/gestionar-compras'
app.register_blueprint(pdcmod, url_prefix=f'{modulo1}/registrar-pedido-compras')




from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.cargo.cargo_api import carapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.persona.persona_api import perapi
from app.rutas.referenciales.turno.turno_api import turapi
from app.rutas.referenciales.dia.dia_api import diaapi
from app.rutas.referenciales.sucursal.sucursal_api import sucapi
from app.rutas.referenciales.horario.horario_api import horapi
from app.rutas.referenciales.tipolesion.tipolesion_api import tipapi
from app.rutas.referenciales.tipoconsulta.tipoconsulta_api import ipoapi
from app.rutas.referenciales.profesional.profesional_api import proapi
from app.rutas.referenciales.departamento.departamento_api import depapi




# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(carapi, url_prefix=version1)
app.register_blueprint(nacapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(perapi, url_prefix=version1)
app.register_blueprint(turapi, url_prefix=version1)
app.register_blueprint(diaapi, url_prefix=version1)
app.register_blueprint(sucapi, url_prefix=version1)
app.register_blueprint(horapi, url_prefix=version1)
app.register_blueprint(tipapi, url_prefix=version1)
app.register_blueprint(ipoapi, url_prefix=version1)
app.register_blueprint(proapi, url_prefix=version1)
app.register_blueprint(depapi, url_prefix=version1)

