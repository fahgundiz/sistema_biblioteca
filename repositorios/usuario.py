from configuracoes.database import conectar
from  interfaces.abstrata_usuario import Abstrata_Usuario

class Repositoriosql(Abstrata_Usuario):
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()

    def criar_usuario(self,nome,email,telefone,cpf):
        sql = """INSERT INTO usuario (nome,email,telefone,cpf)
        VALUES (%s,%s,%s,%s)
        """
        valores = (nome,email,telefone,cpf)
        self.cursor.execute(sql,valores)
        self.conexao.commit()

        print(f"Usuário: {nome} criado com sucesso!")

    def listar_usuarios(self):
        sql = "SELECT idusuario,nome,email,telefone FROM usuario"

        self.cursor.execute(sql)

        usuarios = self.cursor.fetchall()

        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado")
            return
        
        for idusuario,nome,email,telefone in usuarios:
            print(f"ID: {idusuario} | Nome: {nome} | Email: {email} | Telefone: {telefone}")