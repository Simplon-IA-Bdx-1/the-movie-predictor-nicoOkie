import os
import mysql.connector


class Database:
    def connect_to_database():
        password = os.environ["MYSQL_PASSWORD"]
        return mysql.connector.connect(
            user="predictor",
            password=password,
            host="database",
            database="predictor",
        )

    def disconnect_database(cnx):
        cnx.close()

    def create_cursor(cnx):
        return cnx.cursor(dictionary=True)

    def close_cursor(cursor):
        cursor.close()
