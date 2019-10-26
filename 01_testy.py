def funkcja1():
    a = 1
    b = 2
    c = 3
    return a, b, c

def funkcja2(imie, nazwisko, wiek):
    print("Witaj ",imie + nazwisko," cieczymy sie z twojego przybycia,",
          "troche lat juz minelo, nie jestes juz taki mlody. W koncu", wiek,
          "lat na karku to juz nie tak malo")
    

x,y,z = funkcja1()
print(x, '\n')
print(y, '\n')
print(z, '\n')

funkcja2("Marek", "Kowalik", 45)

