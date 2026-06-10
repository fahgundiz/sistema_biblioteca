from configuracoes.database import conectar
from interfaces.abs_livro import Abstrata_Livro

class Repositoriosqlivro(Abstrata_Livro):
    def __init__(self):
      self.conexao = conectar()
      self.cursor = self.conexao.cursor()


    def criar_livro(self, titulo, autor, editora, ano_publicacao, isbn,quantidade_disponivel):
       """
       Efetua a criação do livro, dentro do banco de dados, conforme os
       dados passados para o livro
       sql -> comando que irá ser utilizado para inserir os dados dentro da tabela de livro
       valores -> pega os valores passados para os parametros e adiciona junto aos valores do sql
       por final, efetua um commit, permitindo a inserção dos dados dentro da tabela.
       """
       sql = """INSERT INTO livro (titulo,autor,editora,ano_publicacao,isbn,quant_disponivel)
       VALUES (%s,%s,%s,%s,%s,%s)
       """
       valores = (titulo,autor,editora,ano_publicacao,isbn,quantidade_disponivel)

       self.cursor.execute(sql,valores)
       self.conexao.commit()

       print(f"Livro {titulo} criado com sucesso")

    def listar_livros(self):
       """
       Faz a listagem dos livros
       sql -> comando que irá ser utilizado para selecionar os livros, conforme os dados inseridos
       por final os livros são listados utilizando um loop for, para pegar cada dado do livro e lista-los
       """
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
      """
      Faz a atualização de um livro
      utilizando seu ID para rastrear o livro que pretende ser atualizado
      sql -> Comando que será utilizado para fazer a atualização do livro
      """
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
       """
       Deleta um livro conforme seu ID
       sql = Comando para deletar o livro
       """
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