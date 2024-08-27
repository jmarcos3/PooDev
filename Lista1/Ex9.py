# Herança Multipla

class Movimentavel():
  def mover(self, coordenadas):
    print (f"Movendo {self.nome} para as coodernas: {coordenadas}")

class Desenhavel():
  def desenhar(self):
    print (f"Desenhando {self.nome}..")

class Personagem(Movimentavel,Desenhavel):
  def __init__(self,nome):
    self.nome = nome

personagem = Personagem("Tsurugi")

personagem.desenhar()
personagem.mover("(2,3)")
