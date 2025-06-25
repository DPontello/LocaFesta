from flask import Blueprint, request, jsonify
from models import cliente_model

cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        return jsonify(cliente_model.listar_clientes())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    try:
        cliente = cliente_model.buscar_cliente(id)
        if cliente:
            return jsonify(cliente)
        return jsonify({'error': 'Cliente não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cliente_bp.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    required = ['nomeCliente', 'emailCliente', 'telefoneCliente', 'cpfCnpjCliente']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        cliente_model.criar_cliente(data)
        return jsonify({'success': True, 'message': 'Cliente cadastrado com sucesso'}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    required = ['nomeCliente', 'emailCliente', 'telefoneCliente', 'cpfCnpjCliente']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        rowcount = cliente_model.atualizar_cliente(id, data)
        if rowcount == 0:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Cliente atualizado com sucesso'})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        rowcount = cliente_model.excluir_cliente(id)
        if rowcount == 0:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Cliente excluído com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
