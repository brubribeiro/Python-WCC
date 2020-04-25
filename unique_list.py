#Bruna Ribeiro - 23/11/2019

def unique_list(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
