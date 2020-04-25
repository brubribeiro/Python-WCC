#Bruna Ribeiro - 23/11/2019

def ran_check(num,low,high):
  check = num in range(low,high+1)
  if check == True:
    print(f'{num} in the range between {low} and {high}')
  else:
    print(f'{num} not in range between {low} and {high}')
