#Bruna Ribeiro - 22/11/2019

def summer_letras(lista):
  total = ""
  add = True
  for letra in lista:
    while add:
      if letra != 'd':
        total += letra
        break
      else:
        add = False
    while not add:
      if letra != 'f':
        break
      else:
        add = True
  return total  
