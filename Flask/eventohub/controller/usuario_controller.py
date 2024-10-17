from flask import Blueprint, jsonify, request
from service.usuario_service import UsuarioService
from entity.usuario import Usuario
from exception.usuario_existente_exception import UsuarioExistenteException
usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    print("ID", id)
    try:
        usuario = UsuarioService.buscar_por_id(id)
        return jsonify(usuario.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error":str(e)}), 400

@usuario_bp.route('', methods=['GET'])
def get_usuarios():
    usuarios = UsuarioService.buscar_todos()
    return jsonify(usuarios)

@usuario_bp.route('', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'], cpf=data['cpf'])
    try:
        usuario_salvo = UsuarioService.cadastrar_usuario(usuario)
        return jsonify(usuario_salvo.to_dict()), 201
    except UsuarioExistenteException as uee:
        return jsonify({"Error":str(uee)}), 403
    except ValueError as e:
        return jsonify({"Error":str(e)}), 409
    except Exception as ex:
        return jsonify({"Error":"Error Inesperado, tente novamente mais tarde"}), 500

    return 