from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c81dac792846c247acb200f1b0a7eab4'
client = MongoClient(
    "mongodb+srv://jatobrun:jatobrun@cluster0-hx8rh.mongodb.net/test?retryWrites=true&w=majority")

db = client['Fundacion']
tabla_mascotas = db['Mascotas']
tabla_solicitudes = db['Solicitudes']

from src import routes