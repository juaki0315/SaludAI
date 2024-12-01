from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

# Inicialización de extensiones
mongo = PyMongo()
db = SQLAlchemy()
redis_client = Redis(host='localhost', port=6379, decode_responses=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializar extensiones
    mongo.init_app(app)
    db.init_app(app)
    
    # Registrar rutas
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
    
    return app
