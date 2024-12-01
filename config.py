import os
import redis

class Config:
    # Clave secreta para la seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')

    # Configuración de MongoDB
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/appointments')

    # Configuración de SQLAlchemy (SQLite por defecto)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///chatbot.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de Redis para sesiones
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=int(os.environ.get('REDIS_PORT', 6379)), decode_responses=True)
    
    # Clave API para OpenAI
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'your-openai-api-key')
