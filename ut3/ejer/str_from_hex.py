# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    text = 0
    for code in hex_codes:
        value = chr(int(code, 16))
        text += value
    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])
