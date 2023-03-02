# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    for word in words:
        key = word[0]
        if key in group_words:
            group_words[key].append(word)
        else:
            group_words[key] = [word]

    return group_words


if __name__ == "__main__":
    run(
        [
            "mesa",
            "móvil",
            "barco",
            "coche",
            "avión",
            "bandeja",
            "casa",
            "monitor",
            "carretera",
            "arco",
        ]
    )
