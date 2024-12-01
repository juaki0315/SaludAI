import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/appointments')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///chatbot.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
