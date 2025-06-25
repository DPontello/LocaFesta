from flask import Blueprint, request, jsonify
from models import reserva_model

reserva_bp = Blueprint('reserva_bp', __name__)

@reserva_bp.route('/reservas', methods=['GET'])
def get_reservas():
    try:
        return jsonify(reserva_model.listar_reservas())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reserva_bp.route('/reservas/<int:id>', methods=['GET'])
def get_reserva(id):
    try:
        reserva = reserva_model.buscar_reserva(id)
        if not reserva:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        return jsonify(reserva)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reserva_bp.route('/reservas', methods=['POST'])
def create_reserva():
    data = request.get_json()
    required = ['idCliente', 'idEquipamento', 'dataInicio', 'dataFim', 'status']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        reserva_model.criar_reserva(data)
        return jsonify({'success': True, 'message': 'Reserva criada com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reserva_bp.route('/reservas/<int:id>', methods=['PUT'])
def update_reserva(id):
    data = request.get_json()
    required = ['idCliente', 'idEquipamento', 'dataInicio', 'dataFim', 'status']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        rowcount = reserva_model.atualizar_reserva(id, data)
        if rowcount == 0:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        return jsonify({'success': True, 'message': 'Reserva atualizada com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reserva_bp.route('/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    try:
        rowcount = reserva_model.excluir_reserva(id)
        if rowcount == 0:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        return jsonify({'success': True, 'message': 'Reserva excluída com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
