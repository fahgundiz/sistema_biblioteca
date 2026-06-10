from configuracoes.database import conectar
from interfaces.abs_livro import Abstrata_Livro

class Repositoriosqlivro(Abstrata_Livro):
    def __init__(self):
      self.conexao = conectar()
      self.cursor = self.conexao.cursor()


<<<<<<< HEAD
    def criar_livro(self, titulo, autor, editora, ano_publicacao, isbn, status, idlivro):
=======
    def criar_livro(self, titulo, autor, editora, ano_publicacao, isbn,status):
>>>>>>> 919b72c28ca719ccdc8088366f46e5eb173e3177

       sql = """INSERT INTO livro (titulo,autor,editora,ano_publicacao,isbn)
       VALUES (%s,%s,%s,%s,%s,%s)
       """
       valores = (titulo,autor,editora,ano_publicacao,isbn, status)

       self.cursor.execute(sql,valores)
       self.conexao.commit()

       print(f"Livro {titulo} criado com sucesso")

    def listar_livros(self):

       sql = "SELECT  idlivro,autor,titulo,editora,ano_publicacao,isbn, status FROM livro"

       self.cursor.execute(sql)
       livros = self.cursor.fetchall()

       if len(livros) == 0:
          print("Nenhum livro encontrado")
          return
       else:
          for idlivro,titulo,autor,editora,ano_publicacao,isbn,status in livros:
             print(f"ID: {idlivro}, titulo: {titulo}, autor: {autor}, editora: {editora}, ano de publicação: {ano_publicacao}, isbn: {isbn}, Status: {status}\n")

    def atualizar_livro(self, idlivro, novo_titulo, novo_autor, nova_editora, novo_ano_publicacao, novo_isbn, status):

      sql = """
    UPDATE livro 
    SET isbn = %s,
        titulo = %s,
        autor = %s,
        editora = %s,
        ano_publicacao = %s,
        status = %s
    WHERE idlivro = %s
    """
       
      valores = (novo_isbn,novo_titulo,novo_autor,nova_editora,novo_ano_publicacao,status,idlivro)

      self.cursor.execute(sql,valores)
      self.conexao.commit()

      if self.cursor.rowcount > 0:
          print("Livro atualizado com sucesso!")
      else:
          print("Livro não encontrado")
    
    def deletar_livro(self, idlivro):
       sql = """
       DELETE FROM livro
       WHERE idlivro = %s
       """

       valores = (idlivro,)

       self.cursor.execute(sql,valores)

       self.conexao.commit()

       if self.cursor.rowcount > 0:
         print("Livro deletado com sucesso!")
       else:
          print("Livro não encontrado")

