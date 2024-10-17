from db import db
import os

# Verifica se o banco de dados já foi criado
def init_db(app):
    db_file = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgresql://', '')

    # Se o arquivo do banco de dados não existir, ele será criado
    if not os.path.exists(db_file):
        print("Creating database...")
        with app.app_context():
            db.create_all()
        print("Database created!")
    else:
        print("Database already exists!")

if __name__ == '__main__':
    init_db()