from .models import db, ChatLog

def process_symptoms(symptoms):
    # Aquí implementarías tu lógica real de chatbot
    response = f"No puedo diagnosticarte, pero con base en tus síntomas ('{symptoms}'), recomiendo que consultes a un médico."
    
    # Guardar en SQL
    chat_log = ChatLog(
        username='anonymous',  # Puedes reemplazar con el usuario real
        symptoms=symptoms,
        response=response
    )
    db.session.add(chat_log)
    db.session.commit()
    
    return response
