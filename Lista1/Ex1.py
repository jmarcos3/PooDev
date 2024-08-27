#1) Classes e Obhetos Básicos:

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  def exibir(self):
    print("Olá, meu nome é {} e eu tenho {} anos" .format(self.nome, self.idade))


pessoa1 = Pessoa("José",20);

pessoa1.exibir()