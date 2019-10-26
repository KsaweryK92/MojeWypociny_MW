#program ma za zadanie wyswietlanie w losowej koejnosci
#skonczonej listy zdefiniowanych slow

import random

lista = ['kot', 'samochod', 'gruszka', 'dlugopis', 'marchewka', 'aeropres',
         'hulajnoga', 'komputer', 'lewarek', 'gniazdko']
wymieszane = []
k = 0

while lista:
    i = random.randrange(len(lista))
    wymieszane.append(lista[i])
    del lista[i]
    k += 1

print(wymieszane)
input("aby zakonczyc...")
