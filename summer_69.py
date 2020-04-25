#Bruna Ribeiro - 21/11/2019

def summer_69(lista):
  total = 0
  add = True
  for num in lista:
    while add:
      if num != 6:
        total += num
        break
      else:
        add = False
    while not add:
      if num != 9:
        break
      else:
        add = True
  return total  
