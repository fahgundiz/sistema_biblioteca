
class Livro_validate:
    def validar_titulo(titulo):
         """valida o titulo, conferindo se o título foi preenchido ou não, caso não seja preenchido
         retorna um erro de título inválido
         """
         if not titulo:
              raise ValueError("Erro: Título inválido")
         
    def validar_isbn(isbn):
            """valida se o isbn foi preenchido e se o tamanho dele é de 10 caracteres
            ou 13 caracteres
            """
            if isbn:
                 if len(isbn) == 10 or len(isbn) == 13:
                      pass
                 else:
                      raise ValueError("Erro: Tamanho de de isbn inválido")
            else:
                 raise ValueError("Erro: isbn deve ser preenchido")
    def validar_autor(autor):
         """
         verifica se o autor é do valor isdigit ou se o autor não for preenchido
         caso contrario, o código continua o fluxo
         """
         if autor.isdigit() or len(autor) ==0:
              raise ValueError("Erro: Autor inválido")
         
    def validar_editora(editora):
         """
         valida se a editora pertence ao tipo digito ou se não for preenchida
         caso contrario o código segue o fluxo
         """
         if editora.isdigit() or len(editora) == 0:
              raise ValueError("Erro: Valor de editora inválido")
         
    def validar_ano_publicacao(ano_publicacao):
         """
         verifica se o ano de publicação for maior que o ano atual ou se for negativo
         caso contrario, segue o fluxo do código
         """
         if ano_publicacao > 2026:
              raise ValueError("Erro: Ano de publicação precisa ser no máximo 2026")
         elif ano_publicacao <= 0:
              raise ValueError("Erro: Ano de publicação inválido")
  
    def validar_status (status):
         """
         valida se o status está sendo preenchida ou se está com valor negativo
         """
         if not status:
              raise ValueError("Erro: Status deve ser preenchida")
         elif status < 0:
              raise ValueError("Erro: O valor não pode ser menor que zero")