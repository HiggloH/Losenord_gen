import random
import json
import tester
import entropi

# Alla bokstäver
bok = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]

# Alla stora bokstäver
stora_bok = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]

# Alla siffror
alla_siffror = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Övriga karaktärer
alla_tecken = ["!", "@", "#", "£", "¤", "$", "%", "&", "/", "{", "}", "(", ")", "[", "]", "=", "?", '\\', ":", ";", ".",
               ",", ">", "<", "*", "+", "-"]

# Alla möjliga tecken
alla = [
    bok,
    stora_bok,
    alla_siffror,
    alla_tecken
]

#Lista på möjliga tecken
possible_characters = []


# Siffror, stora bokstäver och tecken är ett valbart alternativ i lösenordet men inte små bokstäver
def gen_pass(length, siffror: bool, cap: bool, tecken: bool) -> str:
    password = ""

    # Den första i listan är för små bokstäver och den ska alltid vara sann
    a_tecken: list = ["små", "små"]

    # Lägg till siffror, stora och tecken i listan på möjliga symboler
    if siffror:
        a_tecken.append("siffror")

    if cap:
        a_tecken.append("stora")

    if tecken:
        a_tecken.append("tecken")

    # Ta fram symbol typ och sen en symbol ur den listan
    for element in range(length):
        element_type = a_tecken[random.randint(0, len(a_tecken) - 1)]

        if element_type == "små":
            nytt_element = get_rand_item(bok)
        elif element_type == "stora":
            nytt_element = get_rand_item(stora_bok)
        elif element_type == "siffror":
            nytt_element = get_rand_item(alla_siffror)
        elif element_type == "tecken":
            nytt_element = get_rand_item(alla_tecken)
        else:
            nytt_element = ""

        password += nytt_element

    return password


def get_rand_item(lista) -> str:
    length = len(lista) - 1
    num = random.randint(0, length)

    return lista[num]


def start_gen():
    skriva_eget = str(input("Vill du generera ett lösenord? "))
    possible_characters.extend(bok)

    if skriva_eget == "ja":
        s_input = str(input("Vill du ändra inställningarna för lösenords genereringen? "))

        if s_input == "ja":
            length = int(input("Hur långt ska ditt lösenord vara? "))
            siffror = (input("Vill du ha siffror i lösenordet "))
            if siffror == "ja":
                siffror = True
                possible_characters.extend(alla_siffror)
            else:
                siffror = False
            cap = (input("Vill du ha stora bokstäver i lösenordet "))
            if cap == "ja":
                cap = True
                possible_characters.extend(stora_bok)
            else:
                cap = False
            tecken = (input("Vill du ha tecken i lösenordet "))
            if tecken == "ja":
                tecken = True
                possible_characters.extend(alla_tecken)
            else:
                tecken = False
        else:
            length = 10
            siffror = True
            possible_characters.extend(alla_siffror)
            cap = True
            possible_characters.extend(stora_bok)
            tecken = True
            possible_characters.extend(alla_tecken)

        password = gen_pass(length, siffror, cap, tecken)
        return password
    else:
        password = input("Vad ska ditt lösenord vara? ")

        return password


def check_user(name):
    with open("passwords.json", "r") as file:
        data = json.load(file)

    # Kolla om namnet finns i databasen
    if name in data:
        print("användaren finns")
        password = input("Vad är ditt lösenord? ")

        #Kolla om lösenordet är rätt till användaren
        if tester.tester(name, password):
            print("Lösenordet var correct!")
            fort = input("Vill du byta lösenord ")
            if fort == "ja":
                return True
            else:
                # OM man inte vill byta kör igen
                start()
        else:
            print("Fel lösenord")
            start()
    else:
        print("Användaren finns inte, fortsätter")
        return True


def save(name, password):
    # Gör en json lista av namnet och lösenordet
    data = {
        name: {
            "user": name,
            "password": password
        }
    }

    # Öppna json filen och ta ut data som finns
    with open("passwords.json", "r") as file:
        file_data = json.load(file)

    # Lägg till den nya användaren i json filen
    file_data.update(data)

    # Spara den nya data till filen
    with open("passwords.json", "w") as file:
        json.dump(file_data, file)


def start():
    name = str(input("Skriv ett användarnamn: "))
    # Kolla om användaren finns
    if check_user(name):
        # Om den inte gör det generera ett nytt lösenord
        password = start_gen()
        print("Ditt lösenord är " + password)
        entropi.calculate(possible_characters, password)

        # Spara lösenordet och användarnamnet
        save(name, password)


start()
