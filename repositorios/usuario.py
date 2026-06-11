from configuracoes.database import conectar
from  interfaces.abstrata_usuario import Abstrata_Usuario

class Repositoriosqlusuario(Abstrata_Usuario):
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()
    @staticmethod
    def validar_email(email):
       return "@" in email and "." in email
    
    def criar_usuario(self,nome,email,telefone,cpf,perfil):
        sql = """INSERT INTO usuario (nome,email,telefone,cpf,perfil)
        VALUES (%s,%s,%s,%s,%s)
        """
        valores = (nome,email,telefone,cpf,perfil)
        self.cursor.execute(sql,valores)
        self.conexao.commit()

        print(f"Usuário: {nome}, com o perfil: {perfil} criado com sucesso!")

    def listar_usuarios(self):
        sql = "SELECT idusuario,nome,email,telefone,perfil FROM usuario"

        self.cursor.execute(sql)

        usuarios = self.cursor.fetchall()

        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado")
            return
        
        for idusuario,nome,email,telefone,perfil in usuarios:
            print(f"ID: {idusuario} | Nome: {nome} | Email: {email} | Telefone: {telefone} | Perfil: {perfil}")
        
    def atualizar_usuario(self,
                           idusuario, 
                           novo_nome,
                           novo_email, 
                           novo_telefone, 
                           novo_cpf,
                           novo_perfil
    ):
       sql = """
       UPDATE usuario
       SET nome = %s,
           email = %s,
           telefone = %s,
           cpf = %s,
           perfil = %s
       WHERE idusuario = %s
       """
##teste02
       valores = (
           novo_nome,
           novo_email,
           novo_telefone,
           novo_cpf,
           novo_perfil,
           idusuario
       )
       
       self.cursor.execute(
           sql,
           valores
       )

       self.conexao.commit()
##teste002
       if self.cursor.rowcount > 0:
           print("usuário atualizado com sucesso")
       else:
           print("usuário não encontrado")
    def deletar_usuario(self, idusuario):
        sql = """
        DELETE FROM usuario
        WHERE idusuario = %s
        """

        valores = (idusuario,)

        self.cursor.execute(
            sql,
            valores
        )

        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("usuário deletado com sucesso")
        else:
            print("usuário não encontrado")