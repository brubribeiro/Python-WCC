#Bruna Ribeiro - 23/11/2019

def count_primes(numero):
  lista = list(range(numero))
  nprimos = []
  for num in lista:
    if num > 2 and num % 2 == 0:
      nprimos.append(num)
    elif num > 3 and num % 3 == 0:
      nprimos.append(num)
    elif num > 5 and num % 5 == 0:
      nprimos.append(num)
    elif num > 7 and num % 7 == 0:
      nprimos.append(num)
    elif num < 2:
      nprimos.append(num)
    
  return numero - len(nprimos)


def count_primes1(num):
  primes = [2]
  x = 3
  if num < 2:
    return 0 
  while x <= num:
    for y in range(3,x,2):
      if x % y == 0:
        x += 2
        break
    else:
       primes.append(x)
       x += 2
 
  print(primes)
  return len(primes)


def count_primes2(num):
  primes = [2]
  x = 3
  count = 0
  if num < 2:
    return 0 
  while x <= num:
    for y in range(3,x,2):
        count += 1
        if x % y == 0:
          x += 2
          break
    else:
       primes.append(x)
       x += 2
 
  print(f'count {count}')
  print(primes)
  return len(primes)
