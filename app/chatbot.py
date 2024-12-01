from .models import db, ChatLog

def process_symptoms(symptoms):
    # lógica real de chatbot conectando con API y preprompting
    response = f"No puedo diagnosticarte, pero con base en tus síntomas ('{symptoms}'), recomiendo que consultes a un médico."
    
    # Guardar en SQL
    chat_log = ChatLog(
        username='anonymous',  # reemplazar con el usuario real
        symptoms=symptoms,
        response=response
    )
    db.session.add(chat_log)
    db.session.commit()
    
    return response
