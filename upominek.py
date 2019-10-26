uczniowie = 28
budzet = 0
prezent = 0

while budzet <= 0:
    budzet = input("Podaj ilość zebranych pieniędzy na dzień dzisiejszy: ")
    budzet = float(budzet)
print("Kwota na prezent na ucznia na dzień dzisiejszy wynosi: ", budzet / uczniowie)

while prezent <= 0:
    prezent = input("Podaj kwotę, jaką zamierzasz wydać na prezent dla ucznia: ")
    prezent = float(prezent)

if budzet < prezent * uczniowie:
    print("Musisz zebrać jeszcze:", prezent * uczniowie - budzet, "aby kupić zamierzony prezent")
else:
    print("Masz już wystarczającą ilość środków, aby kupić zammierzony prezent dla każdego ucznia")
