#7)Composição: 

class Motor:
  def __init__(self, numSerie):
    self.numSerie = numSerie

  def ligar(self):
    print("Vrum vrum")

  def desligar(self):
    print("Motor desligado")

class Carro:
  def __init__(self, marca, modelo, numSerie):
    self.marca = marca
    self.modelo = modelo
    self.motor = Motor(numSerie)
  
  def ligar_carro(self):
    print ("Ligando motor do {}" .format(self.modelo))
    self.motor.ligar()
  
  def desligar_carro(self):
    print("Desligando o {}" .format(self.modelo))
    self.motor.desligar()

celta = Carro("chevrolet","celta",15348)

celta.ligar_carro()
celta.desligar_carro()