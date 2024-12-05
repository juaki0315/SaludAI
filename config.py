from redis import Redis
import os

class Config:
    # Clave secreta para la seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')

    # Configuración de MongoDB
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://juaki1502:DOLym8LUvdCv4Dl3@cluster0.ntati.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

    # Configuración de SQLAlchemy (SQLite por defecto)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///chatbot.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de Redis usando la URL proporcionada
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://default:JhYIVoAvPXzpSgweJbxdHLXfxjAwKKLK@autorack.proxy.rlwy.net:30901')
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'session:'  # Prefijo para claves relacionadas con sesiones en Redis
    SESSION_REDIS = Redis.from_url(REDIS_URL, decode_responses=False)

    # Clave API para OpenAI
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'your-openai-api-key')
