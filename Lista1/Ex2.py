#2) Encapsulamento:

class ContaBancaria:
  def __init__(self,saldo):
    self.__saldo = saldo  # o "__" antes da variavel no python serve para indicar que ela é privada
    print("Conta criada com sucesso")
  
  def depositar(self, valor):
    self.__saldo += valor
    print("Deposito de R${} realizado com sucesso" .format(valor))

  def sacar(self, valor):
    if valor <= self.__saldo:
      self.__saldo -= valor
      print("Saque de R${} realizado com sucesso" .format(valor))
    else:
      print("Saldo insuficiente para realizar operação")

  def consultarSaldo(self):
    print("Seu saldo é: R${}" .format(self.__saldo))
  
conta1 = ContaBancaria(100)
conta1.depositar(300)
conta1.consultarSaldo()
conta1.sacar(80)
conta1.consultarSaldo()