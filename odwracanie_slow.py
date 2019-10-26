def odwracanie(text):
    # go for it
    list = text.split(' ')
    for item in list:
        for i in range(len(item)):
            item[i] = item[len(item) - 1 - i]
    return list

tekst = "zdanie testowe dla zadania"
print(odwracanie(tekst))