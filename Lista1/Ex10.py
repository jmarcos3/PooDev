# Classes abstratas
from abc import ABC,abstractmethod

class FormaGeometrica(ABC):
  @abstractmethod
  def calcularArea():
    pass

class Quadrado(FormaGeometrica):
  def __init__(self,lado):
    self.lado = lado

  def calcularArea(self):
    return (self.lado)**2

class Circulo(FormaGeometrica):
  def __init__(self,raio):
    self.raio = raio
  
  def calcularArea(self):
    return (3.14 * (self.raio**2))

quadrado = Quadrado(2)
circulo = Circulo(2)

print(f"Area do quadrado: {quadrado.calcularArea()}")
print(f"Area do circulo: {circulo.calcularArea()}")