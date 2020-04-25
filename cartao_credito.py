#Bruna Ribeiro - 27/11/2019

class CartaoCredito:

  limitecredito = 1000
  saldofatura = 0
  valorparcela = 0

  def __init__(self,nome,cpf):
    self.nome = nome
    self.cpf = cpf
    self.saldofatura = CartaoCredito.saldofatura
    self.limitecredito = CartaoCredito.limitecredito
    self.valorparcela = CartaoCredito.valorparcela

  def aumentarsaldodiminuirlimite(self,valor):
    self.saldofatura = self.saldofatura + valor
    self.limitecredito = self.limitecredito - valor

  def aumentarlimitediminuirsaldo(self,valor):
    self.saldofatura = self.saldofatura - valor
    self.limitecredito = self.limitecredito + valor
  
  def realizarCompra(self, valor):
    if valor > self.limitecredito:
      raise Exception(f'O valor da compra {valor} é maior que o limite!')
    
    self.aumentarsaldodiminuirlimite(valor)

  def cancelarCompra(self, valor):
    if valor > self.saldofatura:
      raise Exception(f'O valor do cancelamento {valor} é maior que o saldo!')
    
    self.aumentarlimitediminuirsaldo(valor)
    
  def pagarFatura(self, valor):
    if valor > self.saldofatura:
      raise Exception(f'O valor do pagamento {valor} é maior que o saldo da fatura!')

    self.aumentarlimitediminuirsaldo(valor)

  def imprimirFatura(self):
    print(f'Saldo fatura: ', self.saldofatura)
    print(f'Limite: ', self.valorparcela)

  def imprimirDadosCliente(self):
    print('Nome: ', self.nome)
    print('CPF: ', self.cpf)
    print('Saldo Fatura: ', self.saldofatura)
    print('Limite Crédito: ', self.limitecredito)

  def parcelarFatura(self, valorpago, quantidadeparcelas):
    self.valorparcela = (self.saldofatura - valorpago)/quantidadeparcelas
    self.saldofatura = self.saldofatura - valorpago
    self.limitecredito = self.limitecredito + valorpago
    print('Valor Parcela: ', self.valorparcela)
    

  def calcularJurosFatura(self):
    pass
