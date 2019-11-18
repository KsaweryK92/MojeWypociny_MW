STEP = 10
LOW = 1
HIGH = 100


def ask_number(question, low, high):
    """Fcja prosi o podanie liczby z zakresu <low; high)"""
    value = None
    while value not in range(low, high+1):
        value = int(input(question))
    return value


def draw_a_number(low, high):
    """Fcja losuje liczbę z zakresu <low; high>"""
    import random
    return random.randint(low, high)


def congrat_winner(step):
    """Fcja do pogratulowania zwyciezcy"""
    print(f'BRAWO! Udało ci się odgadnąć wylosowaną przez mnie liczbę w mniej niż {STEP} kroków. Dokładnie zajęło ci to {step} kroków')


def main():
    """Fcja główna programu"""
    print(f'Witaj w grze "LOSOWA LICZBA", za chwilę wybiorę dla ciebie liczbę z zakresu od {LOW} do {HIGH}\n',
          'Twoim zadaniem będzie odgadnąć wylosowaną liczbę przy jak najmniejszej ilości prób. POWODZENIA !!!\n')
    liczba = draw_a_number(LOW, HIGH)
    for item in range(STEP):
        zgaduj = ask_number(f'Podaj liczbę z zakresu od {LOW} do {HIGH}: ',LOW, HIGH)
        if zgaduj == liczba:
            return congrat_winner(item + 1)
        elif zgaduj > liczba:
            print('Twoja liczba jest większa od wylosowanej')
        else:
            print('Twoja liczba jest mniejsza od wylosowanej')
    print('Przykro mi, nie udało się tym razem, spróbuj ponownie później')

main()