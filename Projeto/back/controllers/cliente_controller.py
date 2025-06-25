from flask import Blueprint, request, jsonify
from models import clienteModel

clienteBp = Blueprint('clienteBp', __name__)

@clienteBp.route('/clientes', methods=['GET'])
def getClientes():
    try:
        return jsonify(clienteModel.listarClientes())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@clienteBp.route('/clientes/<int:id>', methods=['GET'])
def getCliente(id):
    try:
        cliente = clienteModel.buscarCliente(id)
        if cliente:
            return jsonify(cliente)
        return jsonify({'error': 'Cliente não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@clienteBp.route('/clientes', methods=['POST'])
def createCliente():
    data = request.get_json()
    required = ['nomeCliente', 'emailCliente', 'telefoneCliente', 'cpfCnpjCliente']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        clienteModel.criarCliente(data)
        return jsonify({'success': True, 'message': 'Cliente cadastrado com sucesso'}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@clienteBp.route('/clientes/<int:id>', methods=['PUT'])
def updateCliente(id):
    data = request.get_json()
    required = ['nomeCliente', 'emailCliente', 'telefoneCliente', 'cpfCnpjCliente']
    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    try:
        rowcount = clienteModel.atualizarCliente(id, data)
        if rowcount == 0:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Cliente atualizado com sucesso'})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@clienteBp.route('/clientes/<int:id>', methods=['DELETE'])
def deleteCliente(id):
    try:
        rowcount = clienteModel.excluirCliente(id)
        if rowcount == 0:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        return jsonify({'success': True, 'message': 'Cliente excluído com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
