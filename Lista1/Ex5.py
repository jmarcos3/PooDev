#5)Herança Simpples:

class Veiculo:
  def __init__(self,marca,modelo):
    self.marca = marca
    self.modelo = modelo

class Carro(Veiculo):
  def __init__(self,marca,modelo,cor,qtdPortas):
    super().__init__(marca,modelo)
    self.cor = cor
    self.qtdPortas = qtdPortas

carro = Carro("chevrolet","chevet","verde",2)

print(carro.modelo)