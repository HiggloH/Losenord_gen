import math


def calculate(possible_characters, password):
    r = len(possible_characters)
    length = len(password)

    entropi = math.log2(math.pow(length, r))

    check_entropi(entropi)


def check_entropi(entropi_number):
    if 0 <= entropi_number <= 35:
        print("Lösenordet är väldigt svagt")
    elif 36 <= entropi_number <= 59:
        print("Lösenordet är svagt")
    elif 60 <= entropi_number <= 119:
        print("Lösenordet är starkt")
    elif entropi_number >= 120:
        print("Lösenordet är väldigt starkt")
    else:
        print("Entropin är minder än noll något gick fel")
