import random

HUMAN = ''
PC = ''
EMPTY = ' '
dlugosc = 9

def instrukcja():
    """Wyswietlanie instrukcji"""
    print("""
            Jest to gra stara jak swiat czyli KOLKO i KRZYZYK.
            Twoim przeciwnikiem bedzie komputer, zatem nie zawiedz
            nas w pojedynku miedzy krzemowym procesorem a ludzkim mozgiem.\n""")

def whofirst():
    """Ustalenie kolejnosci"""
    print("Musimy ustalic kolejnosc rozrywki to znaczy kto zaczyna pierwszy")
    wybor = None
    while wybor not in [1,2]:
        print("Masz do wyboru dwa zestawy: 1, gdzie ty zaczynasz",
              "lub 2 gdzie to gdzie to PC zacznie rozgrywke")
        wybor = int(input("Ktory zestaw wybierasz: "))
        if wybor == 1:
            hu = 'X'
            pc = '0'
        elif wybor == 2:
            hu = '0'
            pc = 'X'
        else:
            print("Nieprawidlowa wartosc, blad")
    return hu, pc

def plansza():
    """Tworzy plansze do gry"""
    plansza = []
    for i in range(dlugosc):
        plansza.append(EMPTY)
    return plansza

def wyswietl(plansza):
    """Wyswietlanie planszy do gry"""
    print("\n\t", plansza[0], "|", plansza[1], "|", plansza[2])
    print("\t-----------")
    print("\t", plansza[3], "|", plansza[4], "|", plansza[5])
    print("\t-----------")
    print("\t", plansza[6], "|", plansza[7], "|", plansza[8])

def legalmoves(plansza):
    """Funkcja zwraca liste pol do wykonania ruchu"""
    legalmoves = []
    for i in range(dlugosc):
        if plansza[i] == EMPTY:
            legalmoves.append(i)
    return legalmoves

def winner(plansza):
    """Okreslenie zywciezcy"""
    WYGRANA = ((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))
    for i in WYGRANA:
        if (plansza[i[0]] == plansza[i[1]] == plansza[i[2]] != EMPTY):
            zwyciezca = plansza[i[0]]
            return zwyciezca
    if EMPTY not in plansza:
        return TIE

def human(plansza, human):
    """Zwraca ruch czlowieka"""
    legal = legalmoves(plansza)
    move = None
    while move not in legal:
        move = int(input("Podaj wartosc pola, na ktore chcesz postawic swoj zeton: "))
        if move not in legal:
            print("Nieprawidlowa wartosc, sprobuj ponownie.")
    return move

def computer(plansza, computer):
    """Zwraca ruch komputera"""
    legal = legalmoves(plansza)
    move = None
    while move not in legal:
        move = random.randrange(9)
    return move

def nexturn(turn):
    """Zmiana kolejki"""
    if turn == X:
        return 0
    else:
        return X

def congratwinner(winner, human, computer):
    """Pogratulowanie zwyciezcy"""
    if winner != TIE:
        print(winner," zostales zwyciezca tej rozgrywki")
    else:
        print("Mamy REMIS")


def main():
    instrukcja()
    human, computer = ktopierwszy()
    

instrukcja()
HUMAN, PC = whofirst()
plansza = plansza()
wyswietl(plansza)
ruchy = legalmoves(plansza)
print(ruchy)
