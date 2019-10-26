def get_middle(text):
    new = ''
    x = len(text)
    if x % 2 == 1:
        i = int((x-1)/2)
        new = text[i]
    else:
        i = int(x/2)
        new = text[(i-1):(i+1)]
    return new
slowo = "a"
srodek = get_middle(slowo)
print(srodek)