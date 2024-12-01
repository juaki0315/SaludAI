from app import db, create_app

app = create_app()

with app.app_context():
    db.create_all()  # Crear tablas para SQL
    print("Base de datos inicializada")
