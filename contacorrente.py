#Bruna Ribeiro - 29/11/2019

lass ContaCorrente:

  saldoConta = 0

  def __init__(self,nome,depositoInicial):
    self.nome = nome
    self.depositoInicial = depositoInicial
    self.saldoConta = self.depositoInicial
    self.saques = {}
    self.depositos = {}

  '''
  Será utilizado no print(), formato da sala deverá ser o cliente nome {nome} tem o saldo em conta corrente {saldocontacorrente}
  '''
  def __str__(self):
    return "Nome: %s, Saldo da conta: %s" %(self.nome,self.saldoConta)

  '''
  Validar se o valor do Deposito é maior que o saldo da conta
  '''
  def realizarDeposito(self,valorDeposito, data):
    if valorDeposito <= 0:
      raise Exception(f'O valor de deposito deve ser maior que 0(zero)')
    self.saldoConta = self.saldoConta + valorDeposito
    self.depositos[data] = self.valorDeposito

  '''
  Validar se o valor do Saque é maior que o saldo da conta
  '''
  def realizarSaque(self, valorSaque, data):
    if valorSaque > self.saldoConta:
      raise Exception(f'O valor de Saque {valor} é maior que o saldo da conta!')

    self.saldoConta = self.saldoConta - valorSaque
    self.saques[data] = valorSaque

  def imprimirDadosCliente(self):
    print('Nome: ', self.nome)
    print('Saldo da Conta: ', self.saldoConta)

  def imprimirExtrato(self):
    totalSaques = 0
    totalDepositos = 0
    print('Cliente', self.nome)
    print('Saldo', self.saldoConta)
    for dia, valor in self.saques.items():
      totalDepositos = totalDepositos + valor
      print(f'Deposito dia {data} valor {valorDeposito}')
    print(f'Total Saques {totalSaques}')
    print(f'Total Depositos {totalDepositos}')


c = ContaCorrente('Bruna',10)
c.imprimirDadosCliente()
