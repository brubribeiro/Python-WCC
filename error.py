#Bruna Ribeiro - 03/12/2019

try:
  valor = 10
  valor2 = int(input("Digite um valor: "))
  x = valor/valor2
  print(x)
except ZeroDivisionError:
  print('Erro de divisão por zero')
except IOError:
  print('Erro na leitura do arquivo')


try:
  valor = int(input("Digite o primeiro valor:"))
  valor2 = int(input("Digite o segundo valor: "))
  if valor2 == 0:
    break
  x = valor/valor2
  print('O resultado do calculo é {}'.format(x))
except ZeroDivisionError:
  print('Erro de divisão por zero')
except ValueError:
  print('Favor, informar um valor númerico')
finally:
  print('Código finalizado com sucesso!')
