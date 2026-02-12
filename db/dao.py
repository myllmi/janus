import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

config = {
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'host': os.environ['MYSQL_HOST'],
    'database': os.environ['MYSQL_DATABASE'],
    'raise_on_warnings': True
}


class Dao:
    def __init__(self):
        self.db = mysql.connector.connect(**config)

    def get_connection(self):
        return self.db

    @staticmethod
    def commit_tx(conn):
        conn.commit()

    @staticmethod
    def close_connection(conn):
        conn.close()
