from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.tipoconsulta.TipoconsultaDao import TipoconsultaDao

ipoapi = Blueprint('ipoapi', __name__)

# Trae todos los tipoconsultas
@ipoapi.route('/tipoconsultas', methods=['GET'])
def getTipoconsultas():
    ipodao = TipoconsultaDao()

    try:
        tipoconsultas = ipodao.getTipoconsultas()

        return jsonify({
            'success': True,
            'data': tipoconsultas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las tipoconsultas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@ipoapi.route('/tipoconsultas/<int:tipoconsulta_id>', methods=['GET'])
def getTipoconsulta(tipoconsulta_id):
    ipodao = TipoconsultaDao()

    try:
        tipoconsulta = ipodao.getTipoconsultaById(tipoconsulta_id)

        if tipoconsulta:
            return jsonify({
                'success': True,
                'data': tipoconsulta,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipoconsulta con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener tipoconsulta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo tipoconsulta
@ipoapi.route('/tipoconsultas', methods=['POST'])
def addTipoconsulta():
    data = request.get_json()
    ipodao = TipoconsultaDao()

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
        tipoconsulta_id = ipodao.guardarTipoconsulta(descripcion)
        if tipoconsulta_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': tipoconsulta_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el tipoconsulta. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar tipoconsulta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@ipoapi.route('/tipoconsultas/<int:tipoconsulta_id>', methods=['PUT'])
def updateTipoconsulta(tipoconsulta_id):
    data = request.get_json()
    ipodao = TipoconsultaDao()

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
        if ipodao.updateTipoconsulta(tipoconsulta_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': tipoconsulta_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipoconsulta con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar tipoconsulta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@ipoapi.route('/tipoconsultas/<int:tipoconsulta_id>', methods=['DELETE'])
def deleteTipoconsulta(tipoconsulta_id):
    ipodao = TipoconsultaDao()

    try:
        # Usar el retorno de eliminarTipoconsulta para determinar el éxito
        if ipodao.deleteTipoconsulta(tipoconsulta_id):
            return jsonify({
                'success': True,
                'mensaje': f'Tipoconsulta con ID {tipoconsulta_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipoconsulta con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar tipoconsulta: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500