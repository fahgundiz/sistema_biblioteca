
from configuracoes.database import conectar
from interfaces.abstrata_emprestimo import Abstrata_Emprestimo

class RepositoriosqlEmprestimo(Abstrata_Emprestimo):
    def __init__(self):
      self.conexao = conectar()
      self.cursor = self.conexao.cursor()

    def criar_emprestimo(self, idusuario, idlivro, data_emprestimo, data_devolucao):
      

       if idusuario <= 0 or idlivro <= 0:
          print("ID inválido")
          return

       if data_emprestimo == "" or data_devolucao == "":
          print("As datas devem ser informadas")
          return

       self.cursor.execute("SELECT status FROM livro WHERE idlivro = %s", (
       
       idlivro,))


       livro = self.cursor.fetchone()

       if livro is None:
          print("Livro não encontrado")
          return

       if livro[0] <= 0:
          return

       sql = """
       INSERT INTO usuario_has_livro
       (usuario_idusuario, livro_idlivro, data_emprestimo, data_devolucao)
       VALUES (%s,%s,%s,%s)
       """

       valores = (idusuario, idlivro, data_emprestimo, data_devolucao)

       self.cursor.execute(sql, valores)

       self.cursor.execute("""
       UPDATE livro
       SET status = status
       WHERE idlivro = %s
       """, (idlivro,))

       self.conexao.commit()

       print("Empréstimo criado com sucesso")

    def listar_emprestimos(self):
       """
       Lista todos os empréstimos cadastrados no sistema.
       """

       sql = """
       SELECT usuario_idusuario,
              livro_idlivro,
              data_emprestimo,
              data_devolucao
       FROM usuario_has_livro
       """

       self.cursor.execute(sql)
       emprestimos = self.cursor.fetchall()

       if len(emprestimos) == 0:
          print("Nenhum empréstimo encontrado")
          return

       for usuario_idusuario, livro_idlivro, data_emprestimo, data_devolucao in emprestimos:
          print(
             f"ID usuário: {usuario_idusuario}, "
             f"ID livro: {livro_idlivro}, "
             f"data empréstimo: {data_emprestimo}, "
             f"data devolução: {data_devolucao}\n"
          )

    def atualizar_emprestimo(
        self,
        idusuario,
        idlivro,
        nova_data_emprestimo,
        nova_data_devolucao,
        novo_id_usuario,
        novo_id_livro
    ):
       """
       Atualiza os dados de um empréstimo já cadastrado.
       A busca é feita pelo ID do usuário e do livro.
       """

       if idusuario <= 0 or idlivro <= 0:
          print("ID inválido")
          return

       sql = """
       UPDATE usuario_has_livro
       SET usuario_idusuario = %s,
           livro_idlivro = %s,
           data_emprestimo = %s,
           data_devolucao = %s
       WHERE usuario_idusuario = %s
       AND livro_idlivro = %s
       """

       valores = (
          novo_id_usuario,
          novo_id_livro,
          nova_data_emprestimo,
          nova_data_devolucao,
          idusuario,
          idlivro
       )

       self.cursor.execute(sql, valores)
       self.conexao.commit()

       if self.cursor.rowcount > 0:
          print("Empréstimo atualizado com sucesso!")
       else:
          print("Empréstimo não encontrado")

    def cancelar_emprestimo(self, idusuario, idlivro):
        """
        Remove um empréstimo do sistema.
        Também devolve o status do livro ao estoque.
        """

        sql = """
        DELETE FROM usuario_has_livro
        WHERE livro_idlivro = %s
        AND usuario_idusuario = %s
        """

        valores = (idlivro, idusuario)

        self.cursor.execute(sql, valores)

        self.cursor.execute("""
        UPDATE livro
        SET status = status
        WHERE idlivro = %s
        """, (idlivro,))

        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Empréstimo deletado com sucesso!")
        else:
            print("Empréstimo não encontrado")

    def fazer_devolucao(self, idusuario, idlivro):
       """
       Registra a devolução de um livro.
       Atualiza o status do livro.
       """

       sql = """
       DELETE FROM usuario_has_livro
       WHERE usuario_idusuario = %s
       AND livro_idlivro = %s
       """

       valores = (idusuario, idlivro)

       self.cursor.execute(sql, valores)

       self.cursor.execute("""
       UPDATE livro
       SET status = status
       WHERE idlivro = %s
       """, (idlivro,))

       self.conexao.commit()

       if self.cursor.rowcount > 0:
          print("Devolução realizada com sucesso")
       else:
          print("Empréstimo não encontrado")