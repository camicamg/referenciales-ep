from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.tipolesion.TipolesionDao import TipolesionDao

tipapi = Blueprint('tipapi', __name__)

# Trae todos los tipolesiones
@tipapi.route('/tipolesiones', methods=['GET'])
def getTipolesiones():
    tipdao = TipolesionDao()

    try:
        tipolesiones = tipdao.getTipolesiones()

        return jsonify({
            'success': True,
            'data': tipolesiones,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las tipolesiones: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipapi.route('/tipolesiones/<int:tipolesion_id>', methods=['GET'])
def getTipolesion(tipolesion_id):
    tipdao = TipolesionDao()

    try:
        tipolesion = tipdao.getTipolesionById(tipolesion_id)

        if tipolesion:
            return jsonify({
                'success': True,
                'data': tipolesion,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipolesion con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener tipolesion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva tipolesion
@tipapi.route('/tipolesiones', methods=['POST'])
def addTipolesion():
    data = request.get_json()
    tipdao = TipolesionDao()

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
        tipolesion_id = tipdao.guardarTipolesion(descripcion)
        if tipolesion_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': tipolesion_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el tipolesion. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar tipolesion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipapi.route('/tipolesiones/<int:tipolesion_id>', methods=['PUT'])
def updateTipolesion(tipolesion_id):
    data = request.get_json()
    tipdao = TipolesionDao()

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
        if tipdao.updateTipolesion(tipolesion_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': tipolesion_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipolesion con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar tipolesion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipapi.route('/tipolesiones/<int:tipolesion_id>', methods=['DELETE'])
def deleteTipolesion(tipolesion_id):
    tipdao = TipolesionDao()

    try:
        # Usar el retorno de eliminarTipolesion para determinar el éxito
        if tipdao.deleteTipolesion(tipolesion_id):
            return jsonify({
                'success': True,
                'mensaje': f'Tipolesion con ID {tipolesion_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipolesion con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar tipolesion: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500