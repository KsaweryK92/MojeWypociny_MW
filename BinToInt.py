import math
def bintoint(arr):
    sum = 0
    for i  in range(len(arr)):
        y = math.pow(2,i)
        sum += y*arr[4-i]
    return sum

lista = [1, 1 , 1, 0, 1]
liczba = bintoint(lista)
print(liczba)