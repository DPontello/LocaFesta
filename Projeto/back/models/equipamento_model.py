from db import get_db_connection
from mysql.connector import Error

def listar_equipamentos():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipamento ORDER BY idEquipamento")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def buscar_equipamento(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipamento WHERE idEquipamento = %s", (id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def criar_equipamento(data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO equipamento (nomeEquipamento, tipoEquipamento, valorDiaria)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (data['nomeEquipamento'], data['tipoEquipamento'], data['valorDiaria']))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def atualizar_equipamento(id, data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = """
            UPDATE equipamento SET nomeEquipamento = %s, tipoEquipamento = %s, valorDiaria = %s
            WHERE idEquipamento = %s
        """
        cursor.execute(query, (data['nomeEquipamento'], data['tipoEquipamento'], data['valorDiaria'], id))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def excluir_equipamento(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipamento WHERE idEquipamento = %s", (id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
