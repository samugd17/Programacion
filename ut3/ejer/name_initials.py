"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    upper_fullname = fullname.upper()
    separate_elements = upper_fullname.split()
    if len(separate_elements) == 2:
        first_surname = separate_elements[0]
        name = separate_elements[1]
        initials = f"{name[0]}.{first_surname[0]}."
    else:
        name = separate_elements[2]
        first_surname = separate_elements[0]
        second_surname = separate_elements[1]
        initials = f"{name[0]}.{first_surname[0]}.{second_surname[0]}."

    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
