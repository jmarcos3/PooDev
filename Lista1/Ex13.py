# Tratamento de Exceções, exceções personalizadas

class DivisaoError(Exception):
  def __init__(self,msg):
    super().__init__(msg) #chama o construtor da classe Excpetion que é padrão do python

class Divisao:
  @staticmethod
  def dividir(num,denom):
    if denom == 0:
      raise DivisaoError("Não é possivel divir um numero por 0")
    return num/denom
    
try: 
  print(Divisao.dividir(2,1))
  print(Divisao.dividir(2,2))
  print(Divisao.dividir(2,0))
except DivisaoError as e:
  print(f"Erro: {e}")