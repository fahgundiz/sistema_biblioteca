from abc import abstractmethod
from abc import ABC

class Abstrata_Usuario(ABC):
    pass

    @abstractmethod
    def criar_usuario(self, nome, email, telefone, cpf):
        """
        Método abstrato para criar usuário.
        Parametros: nome(string), email(string), telefone(string), cpf(string)
        """
        pass

    @abstractmethod
    def deletar_usuario(self, idusuario):
        """
        Método abstrato para deletar um usuário através do seu ID.
        Parametros: idusuario(INT)
        """
        pass

    @abstractmethod
    def listar_usuarios(self):
        """
        Método abstrato para listar todos os usuários
        Sem parametros
        """
        pass
    
    @abstractmethod
    def atualizar_usuario(self, idusuario, nome, email, telefone, cpf):
        """
        Método abstrato para atualizar um usuário através do seu ID.
        Parametros: idusuario(INT), nome(string), email(string), telefone(string), cpf(string)
        """
        pass