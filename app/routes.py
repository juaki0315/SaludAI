from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import ChatLog, save_appointment, get_user_appointments, cancel_appointment
from .chatbot import get_chatgpt_response

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('routes.landing'))
    return render_template('login.html', title="Inicio de Sesión")

@bp.route('/landing')
def landing():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    return render_template('landing.html', title="Bienvenido")

@bp.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        save_appointment(session['username'], date, time)
        return redirect(url_for('routes.view_appointments'))
    return render_template('calendar.html', title="Gestión de Citas")

@bp.route('/appointments/view')
def view_appointments():
    appointments = get_user_appointments(session['username'])
    return render_template('appointments.html', appointments=appointments, title="Mis Citas")

@bp.route('/appointments/cancel/<appointment_id>')
def cancel(appointment_id):
    cancel_appointment(session['username'], appointment_id)
    return redirect(url_for('routes.view_appointments'))

@bp.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    response = None
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        prompt = f"Eres un chatbot que actúa como un médico virtual. Tu función es enteder los síntomas que el paciente te describa y decirle que enfermedad es posible que tenga y proponerle un tratamiento para que mejore. Si la pregunta del paciente no esta relacionada con síntomas o el ámbito de la salud, deberás contestar que eres un chatbot que solo se dedica a la salud. La consulta del paciente es la siguiente: {symptoms}"
        response = get_chatgpt_response(prompt)
    return render_template('chatbot.html', response=response, title="Chatbot Médico")

@bp.route('/chatbot/history')
def chatbot_history():
    if 'username' not in session:
        return redirect(url_for('routes.login'))
    
    logs = ChatLog.query.filter_by(username=session['username']).order_by(ChatLog.timestamp.desc()).all()
    
    # Filtrar el texto del prompt
    filtered_logs = []
    prefix = "Eres un chatbot que actúa como un médico virtual. Tu función es enteder los síntomas que el paciente te describa y decirle que enfermedad es posible que tenga y proponerle un tratamiento para que mejore. Si la pregunta del paciente no esta relacionada con síntomas o el ámbito de la salud, deberás contestar que eres un chatbot que solo se dedica a la salud. La consulta del paciente es la siguiente: "
    
    for log in logs:
        # Remover el prefijo solo si está presente
        prompt = log.prompt.replace(prefix, "") if log.prompt.startswith(prefix) else log.prompt
        filtered_logs.append({
            'timestamp': log.timestamp,
            'username': log.username,
            'prompt': prompt,
            'response': log.response
        })

    return render_template('chatbot_history.html', chat_logs=filtered_logs, title="Historial de Consultas")

