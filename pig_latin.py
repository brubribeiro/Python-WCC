#Bruna Ribeiro - 14/11/2019

def pig_latin(palavra):
  primeira_letra = palavra[0]

  if primeira_letra.lower() in 'aeiou':
    palavra_retorno = palavra + 'ay'
  else:
    palavra_retorno = palavra[1:] + primeira_letra + 'ay'
  return palavra_retorno
