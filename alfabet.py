def poz_alfabet(text):
    new = ''
    znaki = ":?+=-_!@#$%^&*()[]{};,.<>/' "
    slownik = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'r':'17', 's':'18', 't':'19', 'u':'20', 'w':'21', 'y':'22', 'z':'23'}
    for i in range(len(text)):
        if text[i] in znaki:
            new += ''
        else:
            new += slownik[text[i]]
            new += ' '
    return new

zdanie = 'sunset is near+ -???'
wynik = poz_alfabet(zdanie)
print(wynik)
