from servicos.menu import *


usuario = Repositoriosqlusuario()
livro = Repositoriosqlivro()
emprestimo = RepositoriosqlEmprestimo()
sistema = Sistema(usuario,livro, emprestimo)

sistema.menu()