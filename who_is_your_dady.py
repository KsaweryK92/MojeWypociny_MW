#program ma za zadanie wylosowac z listy naswisk czlowieka i przyporzadkowac
#go jako ojca do podanej przez uzytkownika osoby

import random

NAMES = ("Tom Cruise", "Andrzej Golota", "Donald Trump", "Jerzy Buzek",
         "Wladimir Putin")
lista = {}
wybor = None


while wybor != '0':
    print("""
            0 - zakoncz
            1 - dodaj postac
            2 - wyswietl slownik
            """)
    wybor = input("Jaka akcje podejmiesz w tym momencie? ")
    if wybor == '0':
        print("do widzewa")
    elif wybor == '1':
        first = input("Podaj imie: ")
        last = input("Podaj nazwisko: ")
        name = first + ' ' + last
        dad = random.choice(NAMES)
        lista[name] = dad
        print(name)
        print(dad)
        print(lista)
    elif wybor == '2':
        print(lista)
    else:
        print("Wystapil blad")

input("aby zakonczyc...")
