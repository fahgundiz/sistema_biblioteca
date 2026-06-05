from repositorios.usuario import *
<<<<<<< HEAD
# Certifique-se de importar o repositório de livros também:
# from repositorios.livro import Repositoriosqllivro 

class Sistema:
    def __init__(self, usuario: Repositoriosqlusuario, livro): 
        self.usuario = usuario
        self.livro = livro  # Adicionado para corrigir o erro nos casos 7 e 8

=======
from repositorios.livro import *

class Sistema:
    def __init__(self, usuario:Repositoriosqlusuario, livro:Repositoriosqlivro):
        self.usuario = usuario
        self.livro = livro
    #teste
>>>>>>> 9b142f8ddfe9ae6294dca2bb19e80f3530734d63
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
            print("10 - Realizar devolução livro")
            print("11 - Cancelar emprestimo livro")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ").strip()
            print("="*50)
            
            match opcao:
                case "1":
                    try:
                        nome = input("Digite o nome do usuário: ")
                        email = input("Digite o email: ")
                        telefone = input("Digite o telefone: ")
                        cpf = input("Digite o cpf: ")
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
                        novo_nome = input("Digite o novo nome: ")
                        novo_email = input("Digite o novo e-mail: ")
                        novo_telefone = input("Digite o novo telefone: ")
                        novo_cpf = input("Digite o novo cpf: ")

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

                        self.usuario.deletar_usuario(idusuario)
                        ##
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "5":
                    try:
                      titulo = input("Título: ")
                      if len(titulo) >= 1:
                          pass
                      else:
                          raise ValueError("Erro: Tamanho de título inválido")
                      autor = input("Autor: ")
                      if autor.isdigit():#Coloquei isdigit porque utilizei (isalpha) para fazer a validação, porém não estava deixando dar espaço
                          raise ValueError("Erro: Valor de autor inváldio")
                      editora = input("Editora: ")
                      if editora.isdigit():#Coloquei isdigit porque utilizei (isalpha) para fazer a validação, porém não estava deixando dar espaço
                          raise ValueError("Erro: Valor de editora inválido")
                      ano_publicacao = int(input("Ano de publicação: "))
                      if ano_publicacao > 0 and ano_publicacao <= 2026:
                          pass
                      else:
                          raise ValueError("Erro: Ano inválido")
                      isbn = input("ISBN: ")
                      if len(isbn) >= 10 and isbn.isdigit() and len(isbn) <= 13:
                          pass
                      else:
                          raise ValueError("Erro: Tamanho inválido, digite 13 números")
                      try:
                       quantidade_disponivel = int(input("Quantidade disponível: "))
                      except ValueError:
                          print("Erro: Quantidade inválida")
                      self.livro.criar_livro(titulo,autor,editora,ano_publicacao,isbn,quantidade_disponivel)
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "6":
                    try:
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "7":
                    try:
                        idlivro = int(input("Digite o ID do livro que você deseja atualizar: "))
                        novo_titulo = input("Digite o novo título: ")
                        novo_autor = input("Digite o novo nome do autor: ")
                        nova_editora = input("Digite a nova editora: ")
                        novo_ano_de_identificacao = int(input("Digite o novo ano de identificação: "))
                        novo_isbn = input("Digite o novo ISBN: ")
                        
                        self.livro.atualizar_livro(
                            idlivro, novo_titulo, novo_autor, 
                            nova_editora, novo_ano_de_identificacao, novo_isbn
                        )
                        print("Livro atualizado com sucesso!")
                    except ValueError:
                        print("Erro: Digite um número válido para o ID e o Ano.")
                    except Exception as erro:
                        print(f"Erro inesperado: {erro}")
                        
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
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "10":
                    try:
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "11":
                    try:
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case '0':
                    print("Saindo do programa...")
                    break
                    
                case __:
                    print("opção inválida, digite novamente")
<<<<<<< HEAD
=======

>>>>>>> 9b142f8ddfe9ae6294dca2bb19e80f3530734d63
