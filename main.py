from servicos.menu import *


usuario = Repositoriosqlusuario()
livro = Repositoriosqlivro()
emprestimo = RepositoriosqlEmprestimo()
livro_validate = Livro_validate()
sistema = Sistema(usuario,livro, emprestimo, livro_validate)

sistema.menu()
