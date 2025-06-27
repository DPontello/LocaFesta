from flask import Blueprint, request, jsonify
from models import equipamentoModel
from validators import validarDadosEquipamento

equipamentoBp = Blueprint('equipamentoBp', __name__)

@equipamentoBp.route('/equipamentos', methods=['GET'])
def getEquipamentos():
    try:
        return jsonify(equipamentoModel.listarEquipamentos())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@equipamentoBp.route('/equipamentos/<int:id>', methods=['GET'])
def getEquipamento(id):
    try:
        equipamento = equipamentoModel.buscarEquipamento(id)
        if not equipamento:
            return jsonify({'error': 'Equipamento não encontrado'}), 404
        return jsonify(equipamento)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@equipamentoBp.route('/equipamentos', methods=['POST'])
def createEquipamento():
    data = request.get_json()
    required = ['nomeEquipamento', 'tipoEquipamento', 'valorDiaria']

    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    
    erros = validarDadosEquipamento(data)
    if erros:
        return jsonify({'error': 'Erro de validação: ' + erros}), 400

    try:
        equipamentoModel.criarEquipamento(data)
        return jsonify({'success': True, 'message': 'Equipamento cadastrado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao cadastrar equipamento: {str(e)}'}), 500

@equipamentoBp.route('/equipamentos/<int:id>', methods=['PUT'])
def updateEquipamento(id):
    data = request.get_json()
    required = ['nomeEquipamento', 'tipoEquipamento', 'valorDiaria']
    
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
        
    erros = validarDadosEquipamento(data)
    if erros:
        return jsonify({'error': 'Erro de validação: ' + erros}), 400

    try:
        rowcount = equipamentoModel.atualizarEquipamento(id, data)
        if rowcount == 0:
            return jsonify({'error': 'Equipamento não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Equipamento atualizado com sucesso'})
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar equipamento: {str(e)}'}), 500

@equipamentoBp.route('/equipamentos/<int:id>', methods=['DELETE'])
def deleteEquipamento(id):
    try:
        rowcount = equipamentoModel.excluirEquipamento(id)
        if rowcount == 0:
            return jsonify({'error': 'Equipamento não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Equipamento excluído com sucesso'})
    except Exception as e:
        return jsonify({'error': f'Erro ao excluir equipamento: {str(e)}'}), 500
