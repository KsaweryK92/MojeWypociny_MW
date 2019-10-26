def find_it(seq):
    dic = {}
    for i in range(len(seq)):
        if seq[i] not in dic:
            dic[seq[i]] = 1
        elif seq[i] in dic:
            dic[seq[i]] += 1
    return dic
#    klucze = dic.keys()         #wynik operacji dic.keys() nie jest indeksowany
#    for k in range(len(klucze)):
#        if dic[klucze[k]] % 2 == 1:
#            return dic[klucze[k]]
#        else:
#            return None

#    for k in range(len(seq)):   #sekwencja jest dłuższa niż słownik przez powtarzające się elementy
#        if dic[seq[k]] % 2 == 1:
#            return dic[seq[k]]
#        else:
#            return None
bbb = [1,2,2,3,3,3,1,1,4,4,5,4,5,6,5,6,5,1,3]
dic = find_it(bbb)
print(dic)
