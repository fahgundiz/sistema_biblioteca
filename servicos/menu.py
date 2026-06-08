from repositorios.usuario import *
from repositorios.emprestimo import RepositoriosqlEmprestimo
from datetime import datetime
class Sistema:
    def __init__(self, usuario:Repositoriosqlusuario, emprestimo:RepositoriosqlEmprestimo):
        self.usuario = usuario
        self.emprestimo = emprestimo
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
                        #
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
                        idusuario = int(input("Digite o ID do usuário: "))
                        idlivro = int(input("Digite o ID do livro: "))
                        data_emprestimo_str = input("Digite a data de emprestimo(YYYY-MM-DD): ")
                        data_devolucao_str = input("Digite a data de devolução(YYYY-MM-DD): ")

                        #Converter string para date time
                        data_emprestimo = datetime.strptime(data_emprestimo_str, "%Y-%m-%d")
                        data_devolucao = datetime.strptime(data_devolucao_str, "%Y-%m-%d")

                        #Bota apenas a data (tira a hora)
                        data_emprestimo_date = data_emprestimo.date()
                        data_devolucao_date = data_devolucao.date()
                        #tentativa push
                        self.emprestimo.criar_emprestimo(idusuario, idlivro, data_emprestimo_date, data_devolucao_date)
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


