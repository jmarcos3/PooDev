# Metodos Estáticos

class MatematicaUtil:
  
  @staticmethod
  def quadrado(num):
    return num**2
  
  @staticmethod
  def cubo(num):
    return num**3
  
  @staticmethod
  def raiz(num):
    return num**(1/2)
  
print(f"Quadrado de 4: {MatematicaUtil.quadrado(4)}")
print(f"Cubo de 4: {MatematicaUtil.cubo(4)}")
print(f"Raiz de 4: {MatematicaUtil.raiz(4)}")