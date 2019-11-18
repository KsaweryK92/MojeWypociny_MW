def ask_number(question, low, high, step=1):
    """Pyta użytkownika o wybór numeru z przedziału <low; high)"""
    value = None
    while value not in range(low, high, step):
        value = int(input(question))
    print(value)
    return value


ask_number('Wybierz numer z przedziału <0,4): ', 0, 4)
