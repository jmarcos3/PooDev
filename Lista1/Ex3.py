#3)Contrutores:

class Produto:
  def __init__(self,nome,preco,qtd) -> None:
    self.nome = nome
    self.preco = preco
    self.qtd = qtd

telefone = Produto("telefone",1500,20)
geladeira = Produto("geladeira",2500,5)
monitor = Produto("monitor",700,10)