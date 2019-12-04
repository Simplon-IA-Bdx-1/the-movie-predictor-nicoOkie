from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()


class Database:
    @staticmethod
    def connect_to_database():
        return mysql.connector.connect(
            user="predictor",
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST", "localhost"),
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
