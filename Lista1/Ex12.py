#Enums

from enum import Enum
from typing import Dict # Dict é um dicionario onde ele tem um valor chave, e um correspondente a ele
# Ex: {Segunda: Dentista}, segundo segunda a chave e Dentista o valor, uma string

class DiasDaSemana(Enum):
  SEGUNDA = "Segunda-feira"
  TERÇA = "Terça-feira"
  QUARTA = "Quarta-feira"
  QUINTA = "Quinta-feira"
  SEXTA = "Sexta-feira"
  SABADO = "Sábado"
  DOMINGO = "Domingo"

class Agenda:
  def __init__(self):
    self.compromissos: Dict[DiasDaSemana, str] ={dia: "" for dia in DiasDaSemana}

  def Agendar(self, dia: DiasDaSemana, compromisso: str):
    self.compromissos[dia] = compromisso
  
  def __str__(self):
    resultado = []
    for dia, compromisso in self.compromissos.items():
      resultado.append(f"{dia.value}: {compromisso if compromisso else 'Livre'}")
    
    return "\n".join(resultado)


agenda = Agenda()

agenda.Agendar(DiasDaSemana.SEGUNDA, "Academia")
agenda.Agendar(DiasDaSemana.TERÇA, "Faculdade")
agenda.Agendar(DiasDaSemana.SEXTA, "Natação")

print(agenda)