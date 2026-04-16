from db import db

class Cachorro(db.Model):
    __tablename__ = 'cachorro'

    id = db.Column(db.Integer, primary_Key=True)
    nome = db.Column(db.String(80), nullable=False)
    raça = db.Column(db.Sting(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def json (self):
        return{
            'id':;
        }