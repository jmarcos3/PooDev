# Iteradores e Loops
'''
Implementar a capacidade de "iteração" torna a classe mais poderosa, flexível e compatível com as 
convenções e funcionalidades do python. é uma forma de aprimorar a classe para que ela se comporte
como uma coleção "natural" em Python, o que é útil para projetos maioreso ou mais complexos.
'''

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
  
  # metodo que permite iteração
  def __iter__(self):
    return iter(self.livros) # iterador padrão da lista

livro1  = Livro("Livro1","aventura")
livro2  = Livro("Livro2","romance")

biblioteca = Biblioteca()
biblioteca.addLivro(livro1)
biblioteca.addLivro(livro2)

for livro in biblioteca:
  print(livro)
