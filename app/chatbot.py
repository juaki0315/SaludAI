import openai
from flask import current_app
from .models import db, ChatLog

def get_chatgpt_response(prompt):
    openai.api_key = current_app.config['OPENAI_API_KEY']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message["content"]

        # Guardar log en la base de datos
        chat_log = ChatLog(
            username=session.get('username', 'anon'),
            symptoms=prompt,
            response=result
        )
        db.session.add(chat_log)
        db.session.commit()

        return result
    except Exception as e:
        return f"Error en el chatbot: {str(e)}"
