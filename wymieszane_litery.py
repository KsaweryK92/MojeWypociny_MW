#program ma za zadanie pomieszac litery wylosowanego
#slowa z ograniczonej puli slow

import random

print("teraz nastapi stworzenie listy - a dokladnie mowiac krotki - 5 slow",
      ", z ktorych jedno z nich zostanie wylosowane do wymieszania jego liter")

WORDS = ("telefon", "zmywarka", "mieszkanie", "betoniarka", "amortyzator")

losowe = random.choice(WORDS)
wymieszane = ''

dl = len(losowe)

while losowe:
    x = random.randrange(0,len(losowe))
    wymieszane += losowe[x]
    losowe = losowe[:x] + losowe[x+1:]
    print(wymieszane,"-----",losowe)

print(wymieszane)
input("nacisnij...")
