from dotenv import load_dotenv
import os

load_dotenv()

class VariablesEnviroment():
    __SERVER_DEBUG = bool(eval(os.getenv("DEBUG").replace(" ", "").capitalize()))
    __HOST_DB = os.getenv("HOST")
    __PORT_DB = int(os.getenv("PORT"))
    __NAME_DB = os.getenv("NAME_DBS")
    __USER_DB = os.getenv("USER")
    __PASSWORD_DB = os.getenv("PASSWORD")
    __SECRET_KEY = os.getenv("SECRET_KEY")
    
    def get_data_server(self) -> dict:
        return {
            "debug": self.__SERVER_DEBUG
        }
    
    def get_data_database(self) -> dict:
        return {
            'host': self.__HOST_DB,
            'port' : self.__PORT_DB,
            'database': self.__NAME_DB,
            'user': self.__USER_DB,
            'password': self.__PASSWORD_DB
        }
    
    def get_data_app(self) -> dict:
        return {
            'SECRET_KEY': self.__SECRET_KEY
        }