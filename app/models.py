from . import mongo, db
from datetime import datetime

# MongoDB: Guardar cita
def save_appointment(username, date, time):
    collection = mongo.db.appointments
    collection.insert_one({
        'username': username,
        'date': date,
        'time': time,
        'created_at': datetime.utcnow()
    })

# MongoDB: Obtener citas
def get_user_appointments(username):
    collection = mongo.db.appointments
    return list(collection.find({'username': username}))

# MongoDB: Cancelar cita
def cancel_appointment(username, appointment_id):
    collection = mongo.db.appointments
    collection.delete_one({'_id': appointment_id, 'username': username})

# SQL: Chatbot consultas y respuestas
class ChatLog(db.Model):
    __tablename__ = 'chat_logs'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
