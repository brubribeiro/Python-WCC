#Bruna Ribeiro - 23/11/2019

def print_big(letter):
  patterns = {0:' ',1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'****',6:'   * ',7:' *   ',8:'*    '}
  alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,8,8,4],'D':[5,3,3,3,5], 'E':[4,8,4,8,4]}
  for pattern in alphabet[letter.upper()]:
    print(patterns[pattern])
