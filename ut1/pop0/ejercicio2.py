# ut1-pop0-ej2
adn = "GGTTACCAACCCAGTCGAAGGTCATGAAGGGGCGTATTTGGATGGAGCTG"
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
length_word = len(adn)
adenines_rate = adn.count("A") / length_word * 100
thymines_rate = adn.count("T") / length_word * 100
guanines_rate = adn.count("G") / length_word * 100
cytosines_rate = adn.count("C") / length_word * 100
# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert adenines_rate == 24.0
assert thymines_rate == 22.0
assert guanines_rate == 36.0
assert cytosines_rate == 18.0