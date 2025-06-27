from flask import Blueprint, request, jsonify
from models import reservaModel
from validators import validarDadosReserva

reservaBp = Blueprint('reservaBp', __name__)

@reservaBp.route('/reservas', methods=['GET'])
def getReservas():
    try:
        return jsonify(reservaModel.listarReservas())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reservaBp.route('/reservas/<int:id>', methods=['GET'])
def getReserva(id):
    try:
        reserva = reservaModel.buscarReserva(id)
        if not reserva:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        return jsonify(reserva)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reservaBp.route('/reservas', methods=['POST'])
def createReserva():
    data = request.get_json()
    required = ['idCliente', 'idEquipamento', 'dataInicio', 'dataFim', 'status']

    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
        
    erros = validarDadosReserva(
        data,
        verificarConflito = lambda idEquipamento, dataInicio, dataFim: 
            reservaModel.verificarConflitoReserva(idEquipamento, dataInicio, dataFim)
    )

    if erros:
        return jsonify({'error': 'Erro de validação', 'detalhes': erros}), 400

    try:
        reservaModel.criarReserva(data)
        return jsonify({'success': True, 'message': 'Reserva criada com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reservaBp.route('/reservas/<int:id>', methods=['PUT'])
def updateReserva(id):
    data = request.get_json()
    required = ['idCliente', 'idEquipamento', 'dataInicio', 'dataFim', 'status']

    if not all(field in data for field in required):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
        
    erros = validarDadosReserva(
        data,
        verificarConflito = lambda idEquipamento, dataInicio, dataFim: 
            reservaModel.verificarConflitoReserva(idEquipamento, dataInicio, dataFim)
    )

    if erros:
        return jsonify({'error': 'Erro de validação', 'detalhes': erros}), 400

    try:
        rowcount = reservaModel.atualizarReserva(id, data)
        if rowcount == 0:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        return jsonify({'success': True, 'message': 'Reserva atualizada com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reservaBp.route('/reservas/<int:id>', methods=['DELETE'])
def deleteReserva(id):
    try:
        rowcount = reservaModel.excluirReserva(id)
        if rowcount == 0:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        return jsonify({'success': True, 'message': 'Reserva excluída com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
