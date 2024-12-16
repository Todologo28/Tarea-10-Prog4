from flask import Blueprint, request, jsonify
from pymongo import MongoClient

# Inicializamos el Blueprint para las rutas de la API
api_bp = Blueprint('api', __name__)

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['mydatabase']
collection = db['recipes']

# Ruta para obtener todas las recetas
@api_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = list(collection.find())
    return jsonify(recipes)

# Ruta para crear una receta
@api_bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe = {
        'name': data['name'],
        'ingredients': data['ingredients'],
        'steps': data['steps']
    }
    collection.insert_one(recipe)
    return jsonify(recipe), 201
