#4)Métodos e Sobrecarga:

class Calculadora:
  @staticmethod
  def soma(*args):
    resultado = args[0]

    for numero in args[1:]:
      resultado += numero

    return resultado
  
  @staticmethod
  def sub(*args):
    resultado = args[0]
    
    for numero in args[1:]:     # esse 1: indica que vai do 1 até o final da lista/tupla
      resultado -= numero
    
    return resultado
  
  @staticmethod
  def mult(*args):
    resultado = args[0]

    for numero in args[1:]:
      resultado *= numero

    return resultado

  @staticmethod
  def div(*args):
    resultado = args[0]

    for numero in args[1:]:
      resultado /= numero
    
    return resultado
  

print(Calculadora.soma(1,2,3,4))
print(Calculadora.sub(5,-3,1))
print(Calculadora.mult(1,2,3,4))
print(Calculadora.div(10,2,5))