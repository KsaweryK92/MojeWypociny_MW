#program ma za zadanie odwrocic podany przez uzytkownika napis

slowo = input("podaj slowo/wyrazenie do odwrocenia: ")
dl = len(slowo)

for i in range(1,dl+1):
    print(slowo[-i])

print("a teraz slowo/napis bez znakow interp.")

slownik = "_-/\[]{}() '\"<>,.?!@%&+="
new = ''

for j in slowo:
    if j not in slownik:
        new += j
        
dl_new = len(new)

for k in range(1,dl_new+1):
    print(new[-k])


input("aby zakonczyc nacisnij...")
