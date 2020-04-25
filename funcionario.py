#Bruna Ribeiro - 28/11/2019

from abc import ABC, abstractmethod
import random

class Funcionario(ABC):

  lista_seq = []
  
  def __init__(self, nome):
    print('Funcionario criado')
    print('Cargo', self.__class__.__name__)
    self.cargo = self.__class__.__name__ 
    try:
      current_id = max(Funcionario.lista_seq,default=0)
    except ValueError:
      current_id = default

    current_id += 1
    Funcionario.lista_seq.append(current_id)

  def __str__(self):
    pass
  
  def __del__(self):
    pass

  def contratar(self, valorHora, quantidadeHoras):
    pass

  def realizarPagamento(self):
    pass

  def pedirAdiantamento(self, valorAdiantamento, data):
    pass

  def imprimirHolerite(self):
    pass

class FuncionarioPorHora(Funcionario):

  def __init__(self, nome):
    Funcionario.__init__(self)
    self.nome = nome
    #self.id = random.randint(1,10000)
    self.id = max(Funcionario.lista_seq)
    self.pagamentos = {}
    self.adiantamentos = {}        
    print(f' Funcionario {self.nome} criado com identificação {self.id}')

    '''
    O funcionario {nomeFuncionario} tem o valor hora {valorHora} 
    com a quantidade de horas contratada {quantidadeHoras}, 
    dando um salario mensal de {salarioMensal}

    ''' 
  def __str__(self):
    out = [f"\nFuncionario %s " %(self.nome)] 
    out.append("Identificação %s " %(self.id))
    out.append("Cargo %s " %(self.cargo))
    out.append("Valor hora : %s" %(self.valorHora))
    out.append("Quantidade de horas contratada : %s" %(self.quantidadeHoras))
    out.append("Salario mensal de %s" %(self.salarioMensal))
    out.append("Saldo salario de %s" %(self.saldoSalario))
    return "\n".join(out)

  def __del__(self):
    print("Você está demitido!!")

  def contratar(self, valorHora, quantidadeHoras):
    self.valorHora = valorHora
    self.quantidadeHoras = quantidadeHoras
    #também poderá ser utilizado para o calculo valorHora * quantidadeHoras        
    self.salarioMensal = self.valorHora * self.quantidadeHoras 
    self.saldoSalario = self.salarioMensal
  

  def realizarPagamento(self, data):
    '''
    Método que irá receber o valor do Pagamento e data do pagamento como parametros
    '''
    self.pagamentos[data] = self.saldoSalario
    self.saldoSalario = 0


  def pedirAdiantamento(self, valorAdiantamento, data):
    if valorAdiantamento > self.saldoSalario:
            raise Exception(f'O valor do adiantamento {valorAdiantamento} é maior que saldo do salario {self.salarioMensal}')
            
    self.saldoSalario = self.saldoSalario - valorAdiantamento
    self.adiantamentos[data] = valorAdiantamento

  def realizarAumentoSalario(self, perc):
    self.SalarioMensal = self.SalarioMensal * (1+perc)

  def virarMes(self):
    self.pagamentos = {}
    self.adiantamentos = {}
    self.saldoSalario = self.SalarioMensal

  def imprimirHolerite(self):
    totalPagamentos = 0
    totalAdiantamentos = 0
    print('Funcionario', self.nome)
    print('Saldo Salario ', self.saldoSalario)
    for dia, valor in self.adiantamentos.items():
      totalAdiantamentos += valor
      print(f'Adiantamentos dia {dia} valor {valor}')

    for dia, valor in self.pagamentos.items():
      totalPagamentos += valor
      print(f'Pagamentos dia {dia} valor {valor}')
           
    print(f'Total Adiantamentos {totalAdiantamentos}')
    print(f'Total Pagamentos {totalPagamentos}')


class FuncionarioAssalariado(Funcionario):

  def __init__(self,nome):
    Funcionario.__init__(self,nome)
    self.nome = nome
    #self.id = random.randint(1,10000)
    self.id = max(Funcionario.lista_seq)
    self.pagamentos = {}
    self.adiantamentos = {}
    print(f'Funcionário {self.nome} criado com identificação {self.id}')

  def __str__(self):
    out = [f"\nFuncionario %s " %(self.nome)] 
    out.append("Identificação %s " %(self.id))
    out.append("Cargo %s " %(self.cargo))
    out.append("Salario mensal de %s" %(self.salarioMensal))
    out.append("Saldo salario de %s" %(self.saldoSalario))
    return "\n".join(out)
  
  def __del__(self):
    print("Você está demitido!!")

  def contratar(self, SalarioMensal):
    self.SalarioMensal = self.salarioMensal
    self.saldoSalario = self.salarioMensal

  def realizarPagamento(self, data):
    self.pagamentos[data] = self.saldoSalario
    self.saldoSalario = 0

  def pedirAdiantamento(self, valorAdiantamento, data):
    self.valorAdiantamento = valorAdiantamento
    self.data = data

  def realizarAumentoSalario(self, perc):
    self.SalarioMensal = self.SalarioMensal * (1+perc)

  def virarMes(self):
    self.pagamentos = {}
    self.adiantamentos = {}
    self.saldoSalario = self.SalarioMensal

  def imprimirHolerite(self):
    totalPagamentos = 0
    totalAdiantamentos = 0
    print('Funcionario', self.nome)
    print('Saldo Salario ', self.saldoSalario)
    for dia, valor in self.adiantamentos.items():
      totalAdiantamentos += valor
      print(f'Adiantamentos dia {dia} valor {valor}')

    for dia, valor in self.pagamentos.items():
      totalPagamentos += valor
      print(f'Pagamentos dia {dia} valor {valor}')
           
    print(f'Total Adiantamentos {totalAdiantamentos}')
    print(f'Total Pagamentos {totalPagamentos}')

class Gerente(Funcionario):

  def __init__(self,nome):
    Funcionario.__init__(self,nome)
    self.nome = nome
    #self.id = random.randint(1,10000)
    self.id = max(Funcionario.lista_seq)
    print(f'Funcionário {self.nome} criado com identificação {self.id}')
    #print('Cargo Gerente')
  
  def __del__(self):
    print("Você está demitido!!")

  def contratar(self, valorHora, quantidadeHoras):
    self.valorHora = valorHora
    self.quantidadeHoras = quantidadeHoras
    self.SalarioMensal = self.valorHora * self.quantidadeHoras

  def realizarPagamento(self, valorPagamento, data):
    self.valorPagamento = valorPagamento
    self.data = data

  def pedirAdiantamento(self, valorAdiantamento, data):
    self.valorAdiantamento = valorAdiantamento
    self.data = data

  def imprimirHolerite(self):
    pass

class Executivo(Funcionario):

  def __init__(self,nome):
    Funcionario.__init__(self,nome)
    self.nome = nome
    #self.id = random.randint(1,10000)
    self.id = max(Funcionario.lista_seq)
    print(f'Funcionário {self.nome} criado com identificação {self.id}')
    #print('Cargo Executivo')
  
  def __del__(self):
    print("Você está demitido!!")

  def contratar(self, valorHora, quantidadeHoras):
    self.valorHora = valorHora
    self.quantidadeHoras = quantidadeHoras
    self.SalarioMensal = self.valorHora * self.quantidadeHoras

  def realizarPagamento(self, valorPagamento, data):
    self.valorPagamento = valorPagamento
    self.data = data

  def pedirAdiantamento(self, valorAdiantamento, data):
    self.valorAdiantamento = valorAdiantamento
    self.data = data

  def imprimirHolerite(self):
    pass
