from os import system, name
def reset_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")