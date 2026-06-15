from servicos.menu import *


usuario = Repositoriosqlusuario()
livro = Repositoriosqlivro()
emprestimo = RepositoriosqlEmprestimo()
livro_validate = Livro_validate()
repositorio_livro = Repositoriosqlivro()
sistema = Sistema(usuario,livro, emprestimo, livro_validate, repositorio_livro)

sistema.menu()
