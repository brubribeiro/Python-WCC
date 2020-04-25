#Bruna Ribeiro - 18/11/2019

def primeira_vogal(palavra):
  palavra_retorno = palavra
  for letra in palavra:
    if not letra.lower() in 'aeiou':
      palavra_retorno = palavra_retorno[1:] + letra
    else:
      break
  return palavra_retorno
