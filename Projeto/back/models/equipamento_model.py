from db import getDbConnection

def listarEquipamentos():
    conn = getDbConnection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipamento ORDER BY idEquipamento")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def buscarEquipamento(id):
    conn = getDbConnection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipamento WHERE idEquipamento = %s", (id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def criarEquipamento(data):
    conn = getDbConnection()
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

def atualizarEquipamento(id, data):
    conn = getDbConnection()
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

def excluirEquipamento(id):
    conn = getDbConnection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipamento WHERE idEquipamento = %s", (id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
