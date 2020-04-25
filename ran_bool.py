#Bruna Ribeiro - 23/11/2019


def ran_bool(num,low,high):
  if num <= high and num >= low:
    return True
  else:
    return False


def ran_bool1(num,low,high):
  if num in range(low,high+1):
    return True
  else:
    return False


def ran_bool2(num,low,high): 
  return num in range(low,high+1)
