def unique(list):
    new = list
    for i in range(len(new)-1):
        if new[i] == new[i+1]:
            del new[i+1]
    return new


lista = ['A', 'A', 'A', 'b', 'C', 'B', 'D', 'D']
poprawiona = unique(lista)
print(poprawiona)