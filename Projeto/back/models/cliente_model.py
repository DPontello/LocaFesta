from db import getDbConnection
import mysql.connector

def listarClientes():
    conn = getDbConnection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente ORDER BY idCliente")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def buscarCliente(id):
    conn = getDbConnection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente WHERE idCliente = %s", (id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def criarCliente(data):
    conn = getDbConnection()
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

def atualizarCliente(id, data):
    conn = getDbConnection()
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

def excluirCliente(id):
    conn = getDbConnection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE idCliente = %s", (id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
