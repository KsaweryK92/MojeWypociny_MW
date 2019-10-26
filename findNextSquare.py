import math
def findNextSquare(liczba):
    x = math.sqrt(liczba)
    if (x % 2 == 1) or (x % 2 == 0):
        next = int(math.pow((x+1),2))
        return next
    else:
        return -1

print(findNextSquare(114))