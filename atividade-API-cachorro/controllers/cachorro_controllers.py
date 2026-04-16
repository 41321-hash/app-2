from models.cachorro_models import Cachorro
from db import db
import json
from flask import make_response

def create_cachorro(cachorro_data):
    novo_cachorro = Cachorro(
        nome=cachorro_data['nome'],
        raça=cachorro_data['raça'],
        idade=cachorro_data['idade']
    )
    db.session.add(novo_cachorro)
    db.session.commit()
    
    response = make_response(
        json.dumps({
            'mensagem': 'Cachorro cadastrado com sucesso!',
            'cachorro': novo_cachorro.json()
        }, sort_keys=False)
    ) # <--- Estava faltando fechar o parênteses corretamente aqui
    
    response.headers['Content-Type'] = 'application/json'
    return response

# --- AS FUNÇÕES ABAIXO PRECISAM EXISTIR PARA O IMPORT FUNCIONAR ---

def get_cachorros():
    # Lógica para listar todos os cachorros
    pass

def get_cachorro_by_id(id):
    # Lógica para buscar um por ID
    pass

def update_cachorro(id, data):
    # Lógica para atualizar
    pass

def delete_cachorro(id):
    # Lógica para deletar
    pass