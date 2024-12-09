import cohere
from flask import current_app
from .models import db, ChatLog

def get_chatgpt_response(prompt):
    try:
        cohere_api_key = current_app.config['COHERE_API_KEY']
        co = cohere.Client(cohere_api_key)

        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=150
        )

        result = response.generations[0].text.strip()

        # Guardar log en la base de datos (opcional)
        # chat_log = ChatLog(
        #     username=session.get('username', 'anon'),
        #     symptoms=prompt,
        #     response=result
        # )
        # db.session.add(chat_log)
        # db.session.commit()

        return result
    except Exception as e:
        return f"Error en el chatbot: {str(e)}"
