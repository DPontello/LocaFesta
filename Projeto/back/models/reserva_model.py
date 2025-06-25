from db import get_db_connection

def listar_reservas():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT r.idReserva, r.dataInicio, r.dataFim, r.status,
                   c.nomeCliente,
                   e.nomeEquipamento
            FROM reserva r
            JOIN cliente c ON r.idCliente = c.idCliente
            JOIN equipamento e ON r.idEquipamento = e.idEquipamento
            ORDER BY r.idReserva
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def buscar_reserva(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT r.idReserva, r.dataInicio, r.dataFim, r.status,
                   r.idCliente, r.idEquipamento
            FROM reserva r
            WHERE r.idReserva = %s
        """
        cursor.execute(query, (id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def criar_reserva(data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reserva (idCliente, idEquipamento, dataInicio, dataFim, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['idCliente'], data['idEquipamento'], data['dataInicio'], data['dataFim'], data['status']))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def atualizar_reserva(id, data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reserva SET idCliente = %s, idEquipamento = %s, dataInicio = %s, dataFim = %s, status = %s
            WHERE idReserva = %s
        """, (data['idCliente'], data['idEquipamento'], data['dataInicio'], data['dataFim'], data['status'], id))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def excluir_reserva(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reserva WHERE idReserva = %s", (id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
