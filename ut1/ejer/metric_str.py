word = "ordenador"
word_lenght = len(word)
a_count = word.count("a")
e_count = word.count("e")
i_count = word.count("i")
o_count = word.count("o")
u_count = word.count("u")
vowels_count = a_count + e_count + i_count + o_count + u_count
metric = word_lenght * vowels_count
print(metric)
