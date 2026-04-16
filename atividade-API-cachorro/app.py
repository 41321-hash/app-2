from flask import Flask
from db import db
from routes.cachorro_routes import cachorro_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cachorro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(cachorro_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)