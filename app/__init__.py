from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

# Inicialización de extensiones
mongo = PyMongo()
db = SQLAlchemy()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar extensiones
    mongo.init_app(app)
    db.init_app(app)

    # Configurar sesiones con Redis
    Session(app)

    # Registrar rutas
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
