from flask import Blueprint, request, jsonify
from models import equipamento_model

equipamento_bp = Blueprint('equipamento_bp', __name__)

@equipamento_bp.route('/equipamentos', methods=['GET'])
def get_equipamentos():
    try:
        return jsonify(equipamento_model.listar_equipamentos())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@equipamento_bp.route('/equipamentos/<int:id>', methods=['GET'])
def get_equipamento(id):
    try:
        equipamento = equipamento_model.buscar_equipamento(id)
        if not equipamento:
            return jsonify({'error': 'Equipamento não encontrado'}), 404
        return jsonify(equipamento)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@equipamento_bp.route('/equipamentos', methods=['POST'])
def create_equipamento():
    data = request.get_json()
    required = ['nomeEquipamento', 'tipoEquipamento', 'valorDiaria']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        equipamento_model.criar_equipamento(data)
        return jsonify({'success': True, 'message': 'Equipamento cadastrado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao cadastrar equipamento: {str(e)}'}), 500

@equipamento_bp.route('/equipamentos/<int:id>', methods=['PUT'])
def update_equipamento(id):
    data = request.get_json()
    required = ['nomeEquipamento', 'tipoEquipamento', 'valorDiaria']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        rowcount = equipamento_model.atualizar_equipamento(id, data)
        if rowcount == 0:
            return jsonify({'error': 'Equipamento não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Equipamento atualizado com sucesso'})
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar equipamento: {str(e)}'}), 500

@equipamento_bp.route('/equipamentos/<int:id>', methods=['DELETE'])
def delete_equipamento(id):
    try:
        rowcount = equipamento_model.excluir_equipamento(id)
        if rowcount == 0:
            return jsonify({'error': 'Equipamento não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Equipamento excluído com sucesso'})
    except Exception as e:
        return jsonify({'error': f'Erro ao excluir equipamento: {str(e)}'}), 500
