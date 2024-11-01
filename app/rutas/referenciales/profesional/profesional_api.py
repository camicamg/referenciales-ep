from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.profesional.ProfesionalDao import ProfesionalDao

proapi = Blueprint('proapi', __name__)

# Trae todos los profesionales
@proapi.route('/profesionales', methods=['GET'])
def getProfesionales():
    prodao = ProfesionalDao()

    try:
        profesionales = prodao.getProfesionales()

        return jsonify({
            'success': True,
            'data': profesionales,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las profesionales: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@proapi.route('/profesionales/<int:profesional_id>', methods=['GET'])
def getProfesional(profesional_id):
    prodao = ProfesionalDao()

    try:
        profesional = prodao.getProfesionalById(profesional_id)

        if profesional:
            return jsonify({
                'success': True,
                'data': profesional,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el profesional con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener profesional: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo profesional
@proapi.route('/profesionales', methods=['POST'])
def addProfesional():
    data = request.get_json()
    prodao = ProfesionalDao()

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
        profesional_id = prodao.guardarProfesional(descripcion)
        if profesional_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': profesional_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el profesional. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar profesional: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@proapi.route('/profesionales/<int:profesional_id>', methods=['PUT'])
def updateProfesional(profesional_id):
    data = request.get_json()
    prodao = ProfesionalDao()

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
        if prodao.updateProfesional(profesional_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': profesional_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el profesional con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar profesional: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@proapi.route('/profesionales/<int:profesional_id>', methods=['DELETE'])
def deleteProfesional(profesional_id):
    prodao = ProfesionalDao()

    try:
        # Usar el retorno de eliminarProfesional para determinar el éxito
        if prodao.deleteProfesional(profesional_id):
            return jsonify({
                'success': True,
                'mensaje': f'Profesional con ID {profesional_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el profesional con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar profesional: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500