#Bruna Ribeiro - 22/11/2019

def spy_game(lista):
  code = []
  for num in lista:
    if num == 0 or num == 7:
      code.append(num)
  for number in code:
    if code == [0,0,7]:
      return True
    else:
      return False
