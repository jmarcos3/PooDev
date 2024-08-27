# Coleções (ArrayList ou equivalente)

class Livro:
  def __init__(self,nome,genero):
    self.nome = nome
    self.genero = genero
  
  def __str__(self):
    return f"Nome: {self.nome}, Genero: {self.genero}"

class Biblioteca:
  def __init__(self):
    self.livros = []

  def addLivro(self,livro):
    self.livros.append(livro)

  def listarLivros(self):
    for livro in self.livros:
      print(livro)

livro1  = Livro("Livro1","aventura")
livro2  = Livro("Livro2","romance")

biblioteca = Biblioteca()
biblioteca.addLivro(livro1)
biblioteca.addLivro(livro2)

biblioteca.listarLivros()
