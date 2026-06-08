from servicos.menu import *


usuario = Repositoriosqlusuario()
livro = Repositoriosqlivro()
sistema = Sistema(usuario,livro)

sistema.menu()