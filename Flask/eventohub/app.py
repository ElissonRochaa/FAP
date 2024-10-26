from flask import Flask
from config import Config
from db import db
import init_db
from controller.usuario_controller import usuario_bp
from controller.evento_controller import evento_bp
from controller.inscricao_controller import inscricao_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

init_db.init_db(app)

app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
app.register_blueprint(evento_bp, url_prefix='/api/eventos')
app.register_blueprint(inscricao_bp, url_prefix='/api/inscricoes')

if __name__ == "__main__":
    app.run(debug=True)