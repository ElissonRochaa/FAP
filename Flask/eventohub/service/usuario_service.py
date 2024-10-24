from repository.usuario_repository import UsuarioRepository
from entity.usuario import Usuario
from exception.usuario_existente_exception import UsuarioExistenteException

class UsuarioService:

    @staticmethod
    def buscar_por_id(id):
        usuario = UsuarioRepository.get_by_id(id)
        if not usuario:
            raise ValueError("Usuario não cadastrado")
        return usuario
        

    @staticmethod
    def buscar_todos():
        usuarios = UsuarioRepository.get_all()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def cadastrar_usuario(usuario):

        usuario_email = UsuarioRepository.get_by_email(usuario.email)
        
        if usuario_email:
            raise UsuarioExistenteException("Email cadastrado")

        if len(usuario.nome) < 3:
            raise ValueError("Nome do usuario menor que 3 caracteres")

        return UsuarioRepository.create(usuario)