from flask import Flask
from db import db
# 1. Certifique-se de que o import está assim
from routes.cachorro_routes import cachorro_routes 

app = Flask(__name__)

# Configurações básicas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. Inicializa o banco
db.init_app(app)

# 3. Registra as rotas (O pulo do gato está aqui!)
app.register_blueprint(cachorro_routes)

# 4. Cria o banco de dados se não existir
with app.app_context():
    db.create_all()

# Rota de teste para ver se o Flask está respondendo
@app.route('/teste_simples', methods=['POST'])
def teste_simples():
    return {"ok": True}, 200

if __name__ == '__main__':
    app.run(debug=True)