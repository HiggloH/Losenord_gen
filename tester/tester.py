import json


def get_pass(user: str) -> dict:
    with open("../passwords.json", "r") as file:
        data = json.load(file)

    if user in data:
        data = data[user]
    else:
        data = "fel_user"

    return data


def tester(user, password):
    data = get_pass(user)

    if data == "fel_user":
        print("Användaren finns inte")
        return

    if password in data.values():
        print("Korrekt lösenord")
    else:
        print("Fel lösenord")


c_username = input("vad är ditt användarnamn? ")
c_password = input("vad är ditt lösenord? ")

tester(c_username, c_password)
