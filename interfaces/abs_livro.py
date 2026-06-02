from abc import ABC, abstractmethod

class Abstrata_Livro(ABC): 
    
    @abstractmethod
    def criar_livro(self, titulo, autor, editora, ano_publicacao, isbn):
        """
        Método abstrato para criar um livro. 
        Parâmetros: 
        titulo (str) 
        autor (str) 
        editora (str) 
        ano_publicacao (int) 
        isbn (str)
        """
        pass 

    @abstractmethod
    def deletar_livro(self, idlivro):
        """
        Método abstrato para deletar um livro através do seu ID. 
        Parâmetros: 
        idlivro (int)
        """
        pass 

    @abstractmethod
    def listar_livros(self):
        """
        Método abstrato para listar todos os livros. 
        Sem parâmetros.
        """
        pass 

    @abstractmethod
    def atualizar_livro(self, idlivro, titulo, autor, editora, ano_publicacao, isbn):
        """
        Método abstrato para atualizar um livro através do seu ID. 
        Parâmetros: 
        idlivro (int) 
        titulo (str) 
        autor (str) 
        editora (str) 
        ano_publicacao (int) 
        isbn (str)
        """
        pass
