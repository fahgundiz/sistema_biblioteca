from abc import ABC, abstractmethod

class Abstrata_Emprestimo(ABC): 
    
    @abstractmethod
    def criar_emprestimo(self, idusuario, idlivro, data_emprestimo, data_devolucao):
        """
        Método abstrato para criar um empréstimo de livro. 
        Parâmetros: 
        idusuario (int)
        idlivro(int)
        data_emprestimo (date)
        data_devolucao(date)
        """
        pass 

    @abstractmethod
    def cancelar_emprestimo(self, idusuario, idlivro):
        """
        Método abstrato para deletar um empréstimo através do ID do usuário e livro. 
        Parâmetros: 
        idusuario (int)
        idlivro (int)

        """
        pass 

    @abstractmethod
    def listar_emprestimos(self):
        """
        Método abstrato para listar todos os empréstimos. 
        Sem parâmetros.
        """
        pass 

    @abstractmethod
    def atualizar_emprestimo(self, idusuario, idlivro, nova_data_emprestimo, nova_data_devolucao, novo_id_usuario, novo_id_livro):
        """
        Método abstrato para atualizar um empréstimo através do ID do usuário e do livro. 
        Parâmetros: 
        idusuario (int)
        idlivro(int)
        data_emprestimo (date)
        data_devolucao(date)
        """
        pass
    