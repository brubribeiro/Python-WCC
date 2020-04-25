#Bruna Ribeiro - 25/11/2019

import string
string.ascii_lowercase

def pangrama(frase,alfabeto = string.ascii_lowercase):
  alfabeto = set(alfabeto)
  return alfabeto <= set(frase.lower())

pangrama('TV faz quengo explodir com whisky JB')

pangrama('Bancos fúteis pagavam-lhe queijo, whisky e xadrez.')


def pangrama2(frase,alfabeto = string.ascii_lowercase):
  alfabeto = set(alfabeto)
  for char in alfabeto:
    if char not in frase.lower():
      return False
  else:
      return True

pangrama2('Bancos fúteis pagavam-lhe queijo, whisky e xadrez.')
