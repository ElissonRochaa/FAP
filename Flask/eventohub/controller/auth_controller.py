from flask import request, jsonify, Blueprint
from entity.usuario import Usuario
from service.usuario_service import UsuarioService
from exception.usuario_existente_exception import UsuarioExistenteException
from utils.functions import role_required

auth_bp = Blueprint("autenticacao", __name__)


#Endpoint de register
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'], cpf=data['cpf'], role="User")
    try:
        usuario_salvo = UsuarioService.cadastrar_usuario(usuario)
        return jsonify(usuario_salvo.to_dict()), 201
    except UsuarioExistenteException as uee:
        return jsonify({"Error":str(uee)}), 403
    except ValueError as e:
        return jsonify({"Error":str(e)}), 409
    
#Endpoint de register
@auth_bp.route('/register/admin', methods=['POST'])
@role_required(['Admin'])
def register_admin():
    data = request.get_json()
    usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'], cpf=data['cpf'], role="Admin")
    try:
        usuario_salvo = UsuarioService.cadastrar_usuario(usuario)
        return jsonify(usuario_salvo.to_dict()), 201
    except UsuarioExistenteException as uee:
        return jsonify({"Error":str(uee)}), 403
    except ValueError as e:
        return jsonify({"Error":str(e)}), 409

#Endpoint de Login
@auth_bp.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    try:
        token = UsuarioService.autorizacao(data['email'], data['senha'])
        print(token)
        return jsonify({"token": str(token)}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 404