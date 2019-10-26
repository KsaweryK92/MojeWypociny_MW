from random import choice, shuffle
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = UPPERCASE.lower()
DIGITS = "0123456789"
ALL = UPPERCASE + LOWERCASE + DIGITS

def random_password(*, upper, lower, digits, length):
    chars = [
        *(choice(UPPERCASE) for _ in range(upper)),
        *(choice(LOWERCASE) for _ in range(lower)),
        *(choice(DIGITS) for _ in range(digits)),
        *(choice(ALL) for _ in range(length-upper-lower-digits)),
    ]
    # shuffle(chars)
    # return "".join(chars
    return chars

print(random_password(upper=1, lower=1, digits=1, length=8))