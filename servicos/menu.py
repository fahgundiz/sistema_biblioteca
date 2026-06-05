from repositorios.usuario import *
# Certifique-se de importar o repositório de livros também:
# from repositorios.livro import Repositoriosqllivro 

class Sistema:
    def __init__(self, usuario: Repositoriosqlusuario, livro): 
        self.usuario = usuario
        self.livro = livro  # Adicionado para corrigir o erro nos casos 7 e 8

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
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "4":
                    try:
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                        
                case "5":
                    try:
                        pass
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
