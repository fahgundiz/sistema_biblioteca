from configuracoes.database import conectar
from interfaces.abs_livro import Abstrata_Livro

class Repositoriosqlivro(Abstrata_Livro):
    def __init__(self):
      self.conexao = conectar()
      self.cursor = self.conexao.cursor()


    def criar_livro(self, titulo, autor, editora, ano_publicacao, isbn,status):

       sql = """INSERT INTO livro (titulo,autor,editora,ano_publicacao,isbn,status)
       VALUES (%s,%s,%s,%s,%s,%s)
       """

       valores = (titulo,autor,editora,ano_publicacao,isbn,status)

       self.cursor.execute(sql,valores)
       self.conexao.commit()

       print(f"Livro {titulo} criado com sucesso")

    def listar_livros(self):

       sql = "SELECT  idlivro,autor,titulo,editora,ano_publicacao,isbn,quant_disponivel FROM livro"

       self.cursor.execute(sql)
       livros = self.cursor.fetchall()

       if len(livros) == 0:
          print("Nenhum livro encontrado")
          return
       else:
          for idlivro,titulo,autor,editora,ano_publicacao,isbn,quantidade_disponivel in livros:
             print(f"ID: {idlivro}, titulo: {titulo}, autor: {autor}, editora: {editora}, ano de publicação: {ano_publicacao}, isbn: {isbn}, Quantidade disponível: {quantidade_disponivel}\n")

    def atualizar_livro(self, idlivro, novo_titulo, novo_autor, nova_editora, novo_ano_publicacao, novo_isbn,nova_quantidade_disponivel):

      sql = """
    UPDATE livro 
    SET isbn = %s,
        titulo = %s,
        autor = %s,
        editora = %s,
        ano_publicacao = %s,
        quant_disponivel = %s
    WHERE idlivro = %s
    """
       
      valores = (novo_isbn,novo_titulo,novo_autor,nova_editora,novo_ano_publicacao,nova_quantidade_disponivel,idlivro)

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

