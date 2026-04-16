from db import db

class Cachorro(db.Model):
    __tablename__ = 'cachorro'

    # O CORRETO É primary_key (tudo minúsculo)
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    raça = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def json (self):
        return{
            'id': self.id,
            'nome': self.nome,
            'raça': self.raça,
            'idade': self.idade
        }