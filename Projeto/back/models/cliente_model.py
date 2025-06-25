from db import get_db_connection
import mysql.connector
from mysql.connector import Error

def listar_clientes():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente ORDER BY idCliente")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def buscar_cliente(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente WHERE idCliente = %s", (id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def criar_cliente(data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cliente (nomeCliente, emailCliente, telefoneCliente, cpfCnpjCliente)
            VALUES (%s, %s, %s, %s)
        """, (data['nomeCliente'], data['emailCliente'], data['telefoneCliente'], data['cpfCnpjCliente']))
        conn.commit()
    except mysql.connector.IntegrityError:
        raise ValueError("Email, telefone ou CPF/CNPJ já cadastrado")
    finally:
        cursor.close()
        conn.close()

def atualizar_cliente(id, data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cliente SET nomeCliente = %s, emailCliente = %s,
            telefoneCliente = %s, cpfCnpjCliente = %s
            WHERE idCliente = %s
        """, (data['nomeCliente'], data['emailCliente'], data['telefoneCliente'], data['cpfCnpjCliente'], id))
        conn.commit()
        return cursor.rowcount
    except mysql.connector.IntegrityError:
        raise ValueError("Email, telefone ou CPF/CNPJ já cadastrado")
    finally:
        cursor.close()
        conn.close()

def excluir_cliente(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE idCliente = %s", (id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
