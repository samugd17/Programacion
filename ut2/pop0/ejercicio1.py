import sys

import pycheck


def run(text: str) -> str:
    VOWELS = "AEIOUaeiou"
    output = ""
    for char in text:
        if char in VOWELS:
            continue
        output += char

    return output


if __name__ == "__main__":
    pycheck.check("pro.ut2.pop0.ej1", sys.argv, run)
