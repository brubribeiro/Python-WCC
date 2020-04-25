#Bruna Ribeiro - 23/11/2019

def up_low(string):
  upper = 0
  low = 0
  for l in string:
    if l.isupper():
      upper += 1
    elif l.islower():
      low += 1
  print(f'Original String: {string}')
  print(f'Upper: {upper}, Lower: {low}')
  print(f'No. of Upper case characters: {upper}')
  print(f'No. of Lower case characters: {low}')
