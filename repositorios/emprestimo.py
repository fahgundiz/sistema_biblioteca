from configuracoes.database import conectar
from interfaces.abstrata_emprestimo import Abstrata_Emprestimo

class RepositoriosqlEmprestimo(Abstrata_Emprestimo):
    def __init__(self):
      self.conexao = conectar()
      self.cursor = self.conexao.cursor()

    def criar_emprestimo(self, idusuario, idlivro, data_emprestimo, data_devolucao):
       sql = """INSERT INTO usuario_has_livro (usuario_idusuario, livro_idlivro, data_emprestimo, data_devolucao)
       VALUE (%s,%s,%s,%s)
       """
       valores = (idusuario, idlivro, data_emprestimo, data_devolucao)

       self.cursor.execute(sql,valores)
       self.conexao.commit()

       print(f"Empréstimo criado com sucesso")

    def listar_emprestimos(self):
       sql = "SELECT usuario_idusuario, livro_idlivro, data_emprestimo, data_devolucao FROM usuario_has_livro"

       self.cursor.execute(sql)
       emprestimos = self.cursor.fetchall()

       if len(emprestimos) == 0:
          print("Nenhum livro encontrado")
          return
       else:
          for usuario_idusuario, livro_idlivro, data_emprestimo, data_devolucao in emprestimos:
             print(f"ID usuário: {usuario_idusuario}, ID livro: {livro_idlivro}, data empréstimo: {data_emprestimo}, data devolução: {data_devolucao}\n")

    def atualizar_emprestimo(self, idusuario, idlivro, nova_data_emprestimo, nova_data_devolucao, novo_id_usuario, novo_id_livro):
       sql = """
    UPDATE usuario_has_livro 
    SET usuario_idusuario = %s,
        livro_idlivro = %s,
        data_emprestimo = %s,
        data_devolucao = %s,
    WHERE usuario_idusuario = %s AND usuario_idlivro = %
    """
       
       valores = (idusuario, idlivro, nova_data_emprestimo, nova_data_devolucao, novo_id_usuario, novo_id_livro)

       self.cursor.execute(sql,valores)
       self.conexao.commit()

       if self.cursor.rowcount > 0:
          print("Empréstimo atualizado com sucesso!")
       else:
          print("Empréstimo não encontrado")
    
    def cancelar_emprestimo(self, idusuario, idlivro):##Mudar quantidade de livro, se usuario não quiser mais o livro, após ter feito um emprestimo
        pass
        sql = """
       DELETE FROM usuario_has_livro
       WHERE livro_idlivro = %s and usuario_id_usuario = %s
       """

        valores = (idusuario,idlivro)

        self.cursor.execute(sql,valores)

        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Empréstimo deletado com sucesso!")
        else:
            print("Empréstimo não encontrado")

    def fazer_devolucao():##Muda a quantidade de livro, quando o cliente devolver o livro antes da data, permitindo atualizar a quantidade de livro
       pass