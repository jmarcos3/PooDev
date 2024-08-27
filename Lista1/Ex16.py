# Generics

'''
O conceito de generics em POO se refere à capacidade de criar classes e funções que podem operar em
diferentes tipos de dados sem precisar especificar o tipo exato antecipadamente. Em python os
generics são implementados principalmente através da biblioteca 'typing'.

Quando dizemos que uma classe é "genérica", estamos nos referindo a uma classe que pode operar com
diferentes tipos de dados, sem ser restrita a um tipo específico. Em outras palavras, uma classe 
genérica é uma classe parametrizada, onde o tipo de dado que ela manipula é definido no momento em
que a classe é instanciada, em vez de ser definido rigidamente no código da classe.
'''

from typing import TypeVar, Generic, List

T = TypeVar('T')

class Caixa(Generic[T]):
  def __init__(self):
    self.itens: List[T] = []

  def add_item(self, item: T):
    self.itens.append(item)
  
  def rem_item(self) -> T:
    return self.itens.pop()
  
caixaInt = Caixa[int]()
caixaInt.add_item(1)
caixaInt.add_item(2)
print(f"Numero {caixaInt.rem_item()} foi removido com sucesso")

caixaStr = Caixa[str]()
caixaStr.add_item('a')
caixaStr.add_item('b')
print(f"Letra {caixaStr.rem_item()} foi removida com sucesso")