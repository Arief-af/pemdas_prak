import mysql.connector

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="ziaq",
        password="nolepngoding",
        database="kelompok1"
    )