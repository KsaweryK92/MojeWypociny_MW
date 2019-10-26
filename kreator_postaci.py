#w programie uzytkownik przeznacza 30pkt na 4 zdolnosci
#dopuki nie zakonczy on programu, moze dowolnie dodawac i odejmowac
#punkty dowolnej zdolnosci

zdolnosci = {'madrosc' : 0, 'sila' : 0, 'odwaga' : 0, 'spryt' : 0}
punkty = 30
wybor = None
mad = 0
sil = 0
odw = 0
spr = 0

while wybor != '0':
    print("W swoim posiadaniu msz jeszcze: ", punkty - (mad + sil + odw + spr),"punktow/punkty")
    print("Menu programu:")
    print("""
            0 - zakoncz
            1 - zmien podzial punktw
            2 - sprawdz podzial punktow
        """)
    wybor = input("Jaka akcje chcesz teraz podjac? ")

    if wybor == '0':
        print("Do widzewa")
    elif wybor == '1':
        print("Pamietaj, masz jedynie 30 punktow do rozdzielenia")
        mad = int(input("Ile punktow przydzielisz madrosci? "))
        sil = int(input("Ile punktow przydzielisz sile? "))
        odw = int(input("Ile punktow przydzielisz odwadze? "))
        spr = int(input("Ile punktow przydzielisz sprytowi? "))
        if (mad + sil + odw + spr) <= 30:
            zdolnosci['madrosc'] = mad
            zdolnosci['sila'] = sil
            zdolnosci['odwaga'] = odw
            zdolnosci['spryt'] = spr
        else:
            print("Nie masz wystarczajacej ilsoci punktow")
            mad = 0
            sil = 0
            odw = 0
            spr = 0
    elif wybor == '2':
        print(zdolnosci)
    else:
        print("Wystapil blad")

input("aby zakonczyc...")
        
