from repositorios.usuario import *

class Sistema:
    def __init__(self, usuario:Repositoriosql):
        self.usuario = usuario
    
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
                        # nome,email,telefone,cpf
                        nome = input("Digite o nome do usuário: ")
                        email = input("Digite o email: ")
                        telefone = input("Digite o telefone: ")
                        cpf = input("Digite o cpf: ")

                        self.usuario.criar_usuario(nome,email,telefone,cpf)
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
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                case "8":
                    try:
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
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


