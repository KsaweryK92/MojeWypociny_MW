def DNA(dna):
    new = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            new += 'T'
        elif dna[i] == 'T':
            new += 'A'
        elif dna[i] == 'C':
            new += 'G'
        elif dna[i] == 'G':
            new += 'C'
    return new

dna = 'GTAT'
odpowiedz = DNA(dna)
print(odpowiedz)