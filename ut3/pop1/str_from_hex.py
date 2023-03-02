# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:

    for code in range(len(hex_codes)):
        text = chr(int(hex_codes[code], 16))
        print(text)
        
       

    return text


if __name__ == "__main__":
    run(["1f49a", "2728", "1f389", "1f3c6"])
