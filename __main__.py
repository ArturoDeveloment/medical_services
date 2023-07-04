from app import create_app
from config import VariablesEnviroment

variables = VariablesEnviroment()

app = create_app()

if __name__ == '__main__':
    app.run(**variables.get_data_server())
