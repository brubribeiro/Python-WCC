#Bruna Ribeiro - 21/11/2019

def paper_doll(palavra):
  result = ''
  for letra in palavra:
    result += letra * 3
  return result

def paper_doll1(text, quant):
  result = ''
  for char in text:
    result += char * quant
  return result
