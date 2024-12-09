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

class ChatLog(db.Model):
    __tablename__ = 'chat_logs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    username = db.Column(db.Text, nullable = False)
