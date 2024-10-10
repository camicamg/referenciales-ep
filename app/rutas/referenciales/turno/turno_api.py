from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.turno.TurnoDao import TurnoDao

turapi = Blueprint('turapi', __name__)

# Trae todos las turnos
@turapi.route('/turnos', methods=['GET'])
def getTurnos():
    turdao = TurnoDao()

    try:
        turnos = turdao.getTurnos()

        return jsonify({
            'success': True,
            'data': turnos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos las turnos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@turapi.route('/turnos/<int:turno_id>', methods=['GET'])
def getTurno(turno_id):
    turdao = TurnoDao()

    try:
        turno = turdao.getTurnoById(turno_id)

        if turno:
            return jsonify({
                'success': True,
                'data': turno,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el turno con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener turno: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo turno
@turapi.route('/turnos', methods=['POST'])
def addTurno():
    data = request.get_json()
    turdao = TurnoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        descripcion = data['descripcion'].upper()
        turno_id = turdao.guardarTurno(descripcion)
        if turno_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': 
                         turno_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el turno. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar turno: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@turapi.route('/turnos/<int:turno_id>', methods=['PUT'])
def updateTurno(turno_id):
    data = request.get_json()
    turdao = TurnoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    descripcion = data['descripcion']
    try:
        if turdao.updateTurno(turno_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': turno_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el turno con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar turno: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@turapi.route('/turnos/<int:turno_id>', methods=['DELETE'])
def deleteTurno(turno_id):
    turdao = TurnoDao()

    try:
        # Usar el retorno de eliminarTurno para determinar el éxito
        if turdao.deleteTurno(turno_id):
            return jsonify({
                'success': True,
                'mensaje': f'Turno con ID {turno_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el turno con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar turno: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500