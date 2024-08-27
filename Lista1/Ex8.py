#8) Associação e Agregação:

class Aluno:
  def __init__(self,nome,matricula,nota):
    self.nome = nome
    self.matricula = matricula
    self.nota = nota
  
  def __str__ (self):
    return f"Nome: {self.nome}, Marticula: {self.matricula}, Nota: {self.nota}"

class Escola:
  def __init__(self,nome):
    self.nome = nome
    self.alunos = []
  
  def matricularAluno(self,aluno):
    self.alunos.append(aluno)

  def listarAlunos(self):
    for aluno in self.alunos:
      print(aluno)

aluno1 = Aluno("João",1,80)
aluno2 = Aluno("Maria",2,75)
escola = Escola("Escola")
escola.matricularAluno(aluno1)
escola.matricularAluno(aluno2)

escola.listarAlunos()