import os
import mysql.connector


class Database:
    @staticmethod
    def connect_to_database():
        password = os.environ["MYSQL_PASSWORD"]
        return mysql.connector.connect(
            user="predictor",
            password=password,
            host="database",
            database="predictor",
        )

    @staticmethod
    def disconnect_database(cnx):
        cnx.close()

    @staticmethod
    def create_cursor(cnx):
        return cnx.cursor(dictionary=True)

    @staticmethod
    def close_cursor(cursor):
        cursor.close()
