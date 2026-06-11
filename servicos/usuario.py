
class Usuario:
    """
    Classe Usuario cria um usuario com atributos:
    nome (string)
    email (string)
    telefone (string)
    cpf (string)
    """
    def __init__(self, nome:str, email:str, telefone:str, cpf:str, perfil:str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.perfil = perfil
    
    @staticmethod
    def validar_nome(nome:str):
        """
        Método estático para validar um nome
        Retorna verdadeiro se o nome possuir apenas letras e espaços em brancos
        Exemplo válido: gabriel, lucas gabriel, gabriellucas
        """
        if all(letra.isspace() or letra.isalpha() for letra in nome):
            return True
        else:
            raise ValueError("Digite um nome válido")


    @staticmethod
    def validar_email(email:str):
        """
        Método estático para validar um e-mail
        Retorna Verdadeiro caso o e-mail contenha "." e "@"
        Exemplo válido: gabriel@hotmail.comm
        Exemplo falso: gabriel.com
        """
        if "@" in email and "." in email:
            return True
        else:
            raise ValueError("Digite um e-mail válido")
    
    @staticmethod
    def validar_telefone(telefone:str):
        """
        Método estático para validar um telefone
        Retorna Verdadeiro caso o telefone contenha 11 digitos, seja apenas numeros sem espaços e o terceiro digito seja 9.
        O DDD(2 digitos) + 9 digitos do celular 
        Exemplo válido: 51999999999 ou 45988888888
        Exemplo falso: 51-999999999 ou 999999999
        """
        if (telefone.isnumeric() and len(telefone)==11 and telefone[2]=='9'):
            return True
        else:
            raise ValueError("Digite um telefone válido")
    
    @staticmethod
    def validar_tipo_perfil(self, perfil):
        """
        Método estático para validar um tipo de perfil
        Retorna Verdadeiro caso o tipo de perfil seja administrador, funcionario ou cliente
        Exemplo válido: administrador, funcionario ou cliente.
        Exemplo falso: admin, user, func
        """
        perfis_validos = ['administrador', 'funcionario', 'cliente']
        
        if perfil in perfis_validos:
            return True
        else:
            return False
    
    @property
    def cpf(self)-> str:
        """
        Método getter para cpf
        Transforma cpf em privado
        """
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf)->str:
        """
        Método setter para cpf
        Válida o cpf se o cpf possuir 11 digitos e apenas números
        Exemplo válido: 00000000000 ou 11111111111
        Exemplo inválido: 000.000.000-00 ou 000 000 000 00
        """
        if len(novo_cpf)==11 and novo_cpf.isnumeric():
            self.__cpf = novo_cpf
        else:
            raise ValueError("Digite um cpf válido")