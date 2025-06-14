from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'database': 'locafesta',
    'user': 'root',
    'password': 'root',
    'port': 3306
}

def get_db_connection():
    """Criar conexão com o banco de dados"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Erro ao conectar com MySQL: {e}")
        return None

# CRUD Cliente
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Erro de conexão com o banco'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente ORDER BY idCliente")
        clientes = cursor.fetchall()
        return jsonify(clientes)
        
    except Error as e:
        return jsonify({'error': f'Erro no banco de dados: {str(e)}'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    nome = data.get('nomeCliente')
    email = data.get('emailCliente')
    telefone = data.get('telefoneCliente')
    cpf_cnpj = data.get('cpfCnpjCliente')
    
    if not all([nome, email, telefone, cpf_cnpj]):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Erro de conexão com o banco'}), 500
    
    try:
        cursor = connection.cursor()
        query = """INSERT INTO cliente (nomeCliente, emailCliente, telefoneCliente, cpfCnpjCliente) 
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (nome, email, telefone, cpf_cnpj))
        connection.commit()
        
        return jsonify({'success': True, 'message': 'Cliente cadastrado com sucesso'})
        
    except mysql.connector.IntegrityError as e:
        return jsonify({'error': 'Email, telefone ou CPF/CNPJ já cadastrado'}), 400
    except Error as e:
        return jsonify({'error': f'Erro no banco de dados: {str(e)}'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Erro de conexão com o banco'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente WHERE idCliente = %s", (cliente_id,))
        cliente = cursor.fetchone()
        
        if not cliente:
            return jsonify({'error': 'Cliente não encontrado'}), 404
            
        return jsonify(cliente)
        
    except Error as e:
        return jsonify({'error': f'Erro no banco de dados: {str(e)}'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    data = request.get_json()
    nome = data.get('nomeCliente')
    email = data.get('emailCliente')
    telefone = data.get('telefoneCliente')
    cpf_cnpj = data.get('cpfCnpjCliente')
    
    if not all([nome, email, telefone, cpf_cnpj]):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Erro de conexão com o banco'}), 500
    
    try:
        cursor = connection.cursor()
        query = """UPDATE cliente SET nomeCliente = %s, emailCliente = %s, 
                   telefoneCliente = %s, cpfCnpjCliente = %s WHERE idCliente = %s"""
        cursor.execute(query, (nome, email, telefone, cpf_cnpj, cliente_id))
        connection.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Cliente não encontrado'}), 404
            
        return jsonify({'success': True, 'message': 'Cliente atualizado com sucesso'})
        
    except mysql.connector.IntegrityError as e:
        return jsonify({'error': 'Email, telefone ou CPF/CNPJ já cadastrado'}), 400
    except Error as e:
        return jsonify({'error': f'Erro no banco de dados: {str(e)}'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/clientes/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Erro de conexão com o banco'}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cliente WHERE idCliente = %s", (cliente_id,))
        connection.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Cliente não encontrado'}), 404
            
        return jsonify({'success': True, 'message': 'Cliente excluído com sucesso'})
        
    except Error as e:
        return jsonify({'error': f'Erro no banco de dados: {str(e)}'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)