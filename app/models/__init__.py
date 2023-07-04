from mysql.connector import connect
from mysql.connector import MySQLConnection
from config import VariablesEnviroment

enviroment = VariablesEnviroment()

class DataBase():
    __CONN = connect(**enviroment.get_data_database())

    def get_conn(self) -> MySQLConnection:
        return self.__CONN

db = DataBase().get_conn()
