# Desenvolvimento e um Sistema de Gestão de Funcionários

class Funcionario:
  def __init__(self,nome,funcao,cpf,telefone):
    self.nome = nome
    self.funcao = funcao
    self.cpf = cpf
    self.telefone = telefone

  def __str__(self):
    return f"Nome: {self.nome}, Função: {self.funcao}, cpf: {self.cpf}, telefone: {self.telefone}"
    
class Chefe(Funcionario):
  def __init__(self):
    self.funcionarios = []

  def add(self, funcionario: Funcionario):
    self.funcionarios.append(funcionario)

  def rem(self, funcionario: Funcionario):
    for f in self.funcionarios:
      if f.cpf == funcionario.cpf:
        self.funcionarios.remove(f)
        break
      else:
        pass

  def att(self, funcionario: Funcionario, att):
    for f in self.funcionarios:
      if f.cpf == funcionario.cpf:
        if att[0] != f.nome:
          f.nome = att[0]
        
        if att[1]  != f.funcao:
          f.funcao = att[1]
        
        if att[2] != f.telefone:
          f.telefone = att[2]
        break
      else:
        pass

  def listar(self):
    for funcionario in self.funcionarios:
      print(funcionario)

# Criando instâncias de funcionários
funcionario1 = Funcionario("João", "Engenheiro", "123456789", "9999-9999")
funcionario2 = Funcionario("Maria", "Designer", "987654321", "8888-8888")

# Criando instância do chefe e adicionando funcionários
chefe = Chefe()
chefe.add(funcionario1)
chefe.add(funcionario2)

# Listando funcionários antes da atualização
chefe.listar()

# Atualizando o nome e telefone do funcionário João
chefe.att(funcionario1,["João Da Silva","Professor","7777-7777"])

# Listando funcionários após a att
print(f"\nApós Atualização:")
chefe.listar()
