#Bruna Ribeiro - 28/11/2019

class Book:
  def __init__(self,titulo,autor,paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    print(f'O livro %s foi criado!' %self.titulo)
  
  def __str__(self):
    return "O título: %s, autor: %s, páginas: %s" %(self.titulo,self.autor,self.paginas)

  def __len__(self):
    return self.paginas

  def __del__(self):
    print("O livro foi destruído")

book = Book('Python para Análise de dados','McKinney, Wes',616)
print(book)
print(len(book))
del book
