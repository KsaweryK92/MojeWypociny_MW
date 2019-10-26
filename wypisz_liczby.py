#program ten ma za zadanie wypisanie ciagu liczb

start = int(input("podaj liczbe poczatku ciagu: "))
stop = int(input("podaj liczbe konca ciagu: "))
krok = int(input("podaj krok, co ktory ma sie zwiekszac ciag: "))

for i in range(start,stop,krok):
    print(i)

input("aby zakonczyc wciasnij ....")
