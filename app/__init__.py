from flask import Flask
from .models import db
from config import VariablesEnviroment

enviroment = VariablesEnviroment()

app = Flask(__name__)
app.config.update(**enviroment.get_data_app())

def create_app() -> Flask:
    return app