from configuracoes.database import conectar
from interfaces.abstrata_livro import Abstrata_Livro

class Repositoriosqlivro(Abstrata_Livro):
    def __init__(self):
      self.conexao = conectar()
      self.cursor = self.conexao.cursor()


    def criar_livro(self, titulo, autor, editora, ano_publicacao, isbn):

       sql = """INSERT INTO livro (titulo,autor,editora,ano_publicacao,isbn)
       VALUES (%s,%s,%s,%s,%s)
       """

       valores = (titulo,autor,editora,ano_publicacao,isbn)

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

    def atualizar_livro(self, idlivro, novo_titulo, novo_autor, nova_editora, novo_ano_publicacao, novo_isbn, novo_status):

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
       
      valores = (novo_isbn,novo_titulo,novo_autor,nova_editora,novo_ano_publicacao,novo_status,idlivro)

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

    def pegar_status(self,idlivro):
       """
       pega o status do livro pelo id, usando o comando sql através da variavel sql
       armazena o id do livro em valor
       rota a variavel sql com o id do livro
       armazena o status na variavel pega_status
       se estiver disponivel, retorna True, caso contrario, retorna False
       """

       sql = "SELECT status FROM livro WHERE idlivro = %s"

       valor = (idlivro,)

       self.cursor.execute(sql,valor)

       pega_status = self.cursor.fetchone()
       status = True
       if pega_status[0] == "indisponivel":
          status = False
       return status
    
    def alterar_status(self,idlivro):
      """
      Funcao alterar_status, sempre que for chamada, irá alterar o valor do status do livro
      seleciona o status do livro conforme seu id
      adicionamos o status na variavel status_atual
      logo em seguida utilizamos o comando de update para efetuar a alteracao do status do livro
      se estiver disponivel, muda para indisponivel, ou vece-versa.
      """
      sql = """
      SELECT status FROM livro WHERE idlivro = %s
       """
      
      val = (idlivro,)
      self.cursor.execute(sql,val)
      status_atual = self.cursor.fetchone()
      print(f"Status: {status_atual[0]}")

      if status_atual[0] == "disponivel":
       status = "indisponivel"
       sql = """
     UPDATE livro 
     SET status = %s
     WHERE idlivro = %s
     """
       valor = (status,idlivro)
       self.cursor.execute(sql,valor)
       self.conexao.commit()

      elif status_atual[0] == "indisponivel":
       status = "disponivel"
       sql = """
     UPDATE livro 
     SET status = %s
     WHERE idlivro = %s
     """
       valor = (status,idlivro)
       self.cursor.execute(sql,valor)
       self.conexao.commit()


# def main():
#  Repositoriosqlivro.alterar_status()

# if __name__ == "__main__":
#    main()