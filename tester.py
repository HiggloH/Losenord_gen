import json


def get_pass(user: str) -> dict:
    with open("passwords.json", "r") as file:
        data = json.load(file)

    if user in data:
        data = data[user]
    else:
        data = "fel_user"

    return data


def tester(user, password) -> bool:
    data = get_pass(user)

    if data == "fel_user":
        return False

    if password in data.values():
        return True
    else:
        return False
