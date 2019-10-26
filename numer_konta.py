def numer_konta(cc):
    new = ''
    x = len(cc)
    for i in range(x):
        if i < x-4:
            new += '#'
        else:
            new += cc[i]
    return new

numer = "34546758679678qfdacs47"
zaszyfrowany = numer_konta(numer)
print(zaszyfrowany)
