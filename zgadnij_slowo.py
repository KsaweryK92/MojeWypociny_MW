#program ma za zadanie wylosowac slowo z krotki, podac jego dlugosc, a nastepnie
#pozwoli graczowi na zadanie 5 pytan czy podana przez niego litera zawiera sie
#w slowie i w ktorym miejscu

import random

print("teraz nastapi stworzenie listy - a dokladnie mowiac krotki - 5 slow",
      ", z ktorych jedno z nich zostanie wylosowane do odgadniecia")

WORDS = ("telefon", "zmywarka", "mieszkanie", "betoniarka", "amortyzator")
losowe = random.choice(WORDS)
ukryte = '-'*len(losowe)
slownik = ''

print("slowo zawiera ",len(losowe),"liter =>", ukryte)
#print(losowe)

for i in range(5):
    new = ''
    x = input("podaj litere: ")
    slownik += x
    #print(slownik)
    for k in losowe:
        if k in slownik:
            new += k
        else:
            new += '-'
    print(new)

input("aby zakonczyc...")
            
