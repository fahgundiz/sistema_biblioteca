from repositorios.usuario import *
from repositorios.livro import *
from repositorios.emprestimo import *
from .livro_validate import Livro_validate
from servicos.usuario import *
from datetime import datetime

class Sistema:
    def __init__(self, usuario:Repositoriosqlusuario, livro:Repositoriosqlivro, emprestimo:RepositoriosqlEmprestimo, livro_validate: Livro_validate):
        self.usuario = usuario
        self.livro = livro
        self.emprestimo = emprestimo
        self.livro_validate = livro_validate
    #teste

    def menu(self):
        while True:
            print("="*50)
            print("=== MENU SISTEMA ===")
            print("")
            print("1 - Cadastrar usuário")
            print("2 - Listar usuários")
            print("3 - Atualizar usuário")
            print("4 - Deletar usuário")
            print("5 - Cadastrar livro")
            print("6 - Listar livros")
            print("7 - Atualizar livro")
            print("8 - Deletar livro")
            print("9 - Realizar emprestimo livro")
            print("10 - Cancelar emprestimo")
            print("11 - Listar emprestimos")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ").strip()
            print("="*50)
            
            match opcao:
                case "1":
                    try:
                        nome = input("Digite o nome do usuário: ")
                        Usuario.validar_nome(nome)
                        email = input("Digite o email: ")
                        Usuario.validar_email(email)
                        telefone = input("Digite o telefone: ")
                        Usuario.validar_telefone(telefone)
                        cpf = input("Digite o cpf: ")

                        Usuario(nome, email, telefone, cpf)
                        self.usuario.criar_usuario(nome, email, telefone, cpf)
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "2":
                    try:
                        self.usuario.listar_usuarios()
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "3":
                    try:
                        idusuario = int(input("Digite o ID do usuário para atualizar: "))
                        Usuario.validar_idusuario(idusuario)
                        novo_nome = input("Digite o novo nome: ")
                        Usuario.validar_nome(novo_nome)
                        novo_email = input("Digite o novo e-mail: ")
                        Usuario.validar_email(novo_email)
                        novo_telefone = input("Digite o novo telefone: ")
                        Usuario.validar_telefone(novo_telefone)
                        novo_cpf = input("Digite o novo cpf: ")

                        Usuario(novo_nome, novo_email, novo_telefone, novo_cpf)

                        self.usuario.atualizar_usuario(idusuario, 
                           novo_nome,
                           novo_email, 
                           novo_telefone, 
                           novo_cpf)
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "4":
                    try:
                        idusuario = int(input("Digite o ID do usuário para deletar: "))
                        Usuario.validar_idusuario(idusuario)
                        self.usuario.deletar_usuario(idusuario)
                        ##
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "5":
                    try:
                      titulo = input("Título: ")
                      Livro_validate.validar_titulo(titulo)
                      autor = input("Autor: ")
                      Livro_validate.validar_autor(autor)
                      editora = input("Editora: ")
                      Livro_validate.validar_editora(editora)
                      ano_publicacao = int(input("Ano de publicação: "))
                      Livro_validate.validar_ano_publicacao(ano_publicacao)
                      isbn = input("ISBN: ")
                      Livro_validate.validar_isbn(isbn)
                      self.livro.criar_livro(titulo,autor,editora,ano_publicacao,isbn)
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "6":
                    try:
                        self.livro.listar_livros()
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "7":
                        try:
                            idlivro = int(input("Digite o ID do livro que você deseja atualizar: "))
                            novo_titulo = input("Digite o novo título: ")
                            Livro_validate.validar_titulo(novo_titulo)
                            novo_autor = input("Digite o novo nome do autor: ")
                            Livro_validate.validar_autor(novo_autor)
                            nova_editora = input("Digite a nova editora: ")
                            Livro_validate.validar_editora(nova_editora)
                            novo_ano_de_publicacao = int(input("Digite o novo ano de identificação: "))
                            Livro_validate.validar_ano_publicacao(novo_ano_de_publicacao)
                            novo_isbn = input("Digite o novo ISBN: ")
                            Livro_validate.validar_isbn(novo_isbn)
                            self.livro.atualizar_livro(idlivro, novo_titulo, novo_autor,nova_editora, novo_ano_de_publicacao, novo_isbn, nova_quantidade_disponivel)    
                        except Exception as e:
                            print(f"Erro: {e}")           
                            
                case "8":
                    try:
                        idlivro = int(input("Digite o ID do livro que deseja deletar: "))
                        self.livro.deletar_livro(idlivro)
                        print("Livro deletado com sucesso!")
                    except ValueError:
                        print("Erro: O ID deve ser um número inteiro.")
                    except Exception as erro:
                        print(f"Erro inesperado: {erro}")
                        
                case "9":
                    try:
                        idusuario = int(input("Digite o ID do usuário: "))
                        idlivro = int(input("Digite o ID do livro: "))
                        data_emprestimo_str = input("Digite a data de emprestimo(YYYY-MM-DD): ")
                        data_devolucao_str = input("Digite a data de devolução(YYYY-MM-DD): ")

                        #
                        data_emprestimo = datetime.strptime(data_emprestimo_str, "%Y-%m-%d")
                        data_devolucao = datetime.strptime(data_devolucao_str, "%Y-%m-%d")

                        
                        data_emprestimo_date = data_emprestimo.date()
                        data_devolucao_date = data_devolucao.date()
                        
                        self.emprestimo.criar_emprestimo(idusuario, idlivro, data_emprestimo_date, data_devolucao_date)
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "10":
                    try:
                        id_livro = int(input("ID do livro: "))
                        id_usuario = int(input("ID do usuário: "))
                        self.emprestimo.cancelar_emprestimo(id_livro, id_usuario)
                        print("Empréstimo cancelado com sucesso!")
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "11":
                    # try:
                    # except Exception as erro:
                    try:
                        self.emprestimo.listar_emprestimos()
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        ##commit final
                case "12":
                    try:
                      idlivro = int(input("Digite o id do livro: "))
                      self.livro.aumentar_quantidade_livro(idlivro)
                    except Exception as e:
                        print(f"Erro: {e}")
                case '0':
                    print("Saindo do programa...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")