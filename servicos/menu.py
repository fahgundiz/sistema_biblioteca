
class Sistema:
    def __init__(self):
        pass
    
    def menu(self):
        while True:
            print("="*50)
            print("=== MENU SISTEMA  ===")
            print("")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Atualizar cliente")
            print("4 - Deletar cliente")
            print("5 - Cadastrar Médico")
            print("6 - Listar Médicos")
            print("7 - Atualizar Médico")
            print("8 - Deletar Médico")
            print("9 - Criar consulta")
            print("10 - Listar consultas")
            print("11 - Excluir uma consulta")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()
            print("="*50)
            match opcao:

                case "1":
                    try:
                        pass
                    except Exception as erro:
                        print(f"Erro: {erro}")
                case __:
                    print("opção inválida, digite novamente")
