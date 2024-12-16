from flask import Flask
from api import api_bp
import os
from pymongo import MongoClient

app = Flask(__name__)

# Configuración de MongoDB usando variables de entorno
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mydatabase')

# Conectar a MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()

# Registrar las rutas API
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
