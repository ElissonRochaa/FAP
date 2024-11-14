from repository.usuario_repository import UsuarioRepository
from entity.usuario import Usuario
from exception.usuario_existente_exception import UsuarioExistenteException
from exception.usuario_inexistente_exception import UsuarioInexistenteException
from werkzeug.security import generate_password_hash, check_password_hash 
import jwt
from datetime import datetime, timedelta

class UsuarioService:    

    @staticmethod
    def buscar_por_id(id):
        usuario = UsuarioRepository.get_by_id(id)
        if not usuario:
            raise ValueError("Usuario não cadastrado")
        return usuario
        
    @staticmethod
    def autorizacao(email, senha):
        usuario = UsuarioRepository.get_by_email(email)
        if usuario == None:
            raise UsuarioInexistenteException("Email não cadastrado")
        #Teste...
        print("1")
        if check_password_hash(usuario.senha, senha):
            
            payload = {
                'subject': usuario.email,
                'role': usuario.role,
                'exp': datetime.now() + timedelta(hours=4)
            }

            token = jwt.encode(payload, "FAPeventohub", algorithm="HS256")

            return token
        else:
            return ""
        


    @staticmethod
    def buscar_todos():
        usuarios = UsuarioRepository.get_all()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def cadastrar_usuario(usuario):
        
        usuario_email = UsuarioRepository.get_by_email(usuario.email)
        
        if usuario_email:
            print("Entrou aqui...")
            raise UsuarioExistenteException("Email cadastrado")

        if len(usuario.nome) < 3:
            raise ValueError("Nome do usuario menor que 3 caracteres")
        
        #transformar a senha em hash
        senha_hash = generate_password_hash(usuario.senha)
        usuario.senha = senha_hash
        return UsuarioRepository.create(usuario)