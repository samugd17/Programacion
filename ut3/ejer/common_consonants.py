# *******************
# CONSONANTES COMUNES
# *******************


def run_ayoze(text1: str, text2: str) -> str:
    VOWELS = 'aeiou'
    text1 = text1.replace(' ', '')
    text2 = text2.replace(' ', '')
    set1 = set(text1)
    set2 = set(text2)
    cconst = {char for char in set1 & set2 if char not in VOWELS}
    cconst = ''.join(sorted(cconst))
    return cconst


def run_javier(text1: str, text2: str) -> str:
    NOT_VALID_CHARS = set('aeiouAEIOU ')
    result_set = set(text1) & set(text2) - NOT_VALID_CHARS
    cconst = ''.join(sorted(result_set))
    return cconst


def run(text1: str, text2: str) -> str:
    VOWELS = 'aeiou'

    text1 = text1.replace(' ', '')
    text2 = text2.replace(' ', '')
    set1 = {char for char in text1 if char not in VOWELS}
    set2 = {char for char in text2 if char not in VOWELS}
    result_set = set1 & set2
    cconst = ''.join(sorted(result_set))
    return cconst


if __name__ == "__main__":
    run("Flat is better than nested", "Readability counts")
