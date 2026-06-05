from servicos.menu import *


usuario = Repositoriosqlusuario()
emprestimo = RepositoriosqlEmprestimo()
sistema = Sistema(usuario, emprestimo)

sistema.menu()