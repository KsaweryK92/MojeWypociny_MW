dystans = int(input("Jaki dystans przejechales: "))
spalanie_na_sto = 7.5
cena_wahy = 5.24
koszt = dystans * spalanie_na_sto / 100 * cena_wahy
dystans += 20
koszt = dystans * spalanie_na_sto / 100 * cena_wahy
print("Koszt danej podróży, jaki poniesiesz to:", koszt)