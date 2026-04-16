from flask import Blueprint, request, jsonify
from controllers.cachorro_controllers import create_cachorro

# O nome aqui deve bater com o que você importa no app.py
cachorro_routes = Blueprint('cachorro_routes', __name__)

@cachorro_routes.route('/cachorros', methods=['POST'])
def cachorro_post():
    cachorro_data = request.get_json() # Pega os dados do Postman
    return create_cachorro(cachorro_data) # Manda para o seu Controller salvar