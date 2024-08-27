#Polimorfismo:
from abc import ABC  # para permitir a criação de classes abstratas

class Animal(ABC):
  def emitirSom(self):
    print("Som do animal")

class Cachorro(Animal):
  def __init__(self,nome):
    self.nome = nome

  def emitirSom(self):
    print("Au au")

class Gato(Animal):
  def __init__(self,nome):
    self.nome = nome

  def emitirSom(self):
    print("Miau")

toto = Cachorro("toto")
toto.emitirSom()

jerry = Gato("Jerry")
jerry.emitirSom()
