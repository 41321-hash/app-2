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
        },sort_keys=False)
)
response.headers['content-type'] = "application/json"
return response 
