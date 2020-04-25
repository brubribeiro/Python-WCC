#Bruna Ribeiro - 21/11/2019

def blackjack(a,b,c):
  if a == 11 or b == 11 or c == 11:
    return sum((a,b,c)) - 10
  elif sum((a,b,c)) > 21:
    print('BUST')
  else:
    return sum((a,b,c))


def blackjack1(a,b,c):
  soma = sum((a,b,c))
  if 11 in (a,b,c):
    return soma - 10
  elif soma > 21:
    print('BUST')
  else:
    return soma
