#Bruna Ribeiro - 25/11/2019

def palindrome(palavra):
  string = palavra.replace(' ','')
  if string == palavra[::-1]:
    return True
  else:
    return False
