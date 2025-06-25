import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', 3306))
}

def getDbConnection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Erro ao conectar com MySQL: {e}")
        return None
