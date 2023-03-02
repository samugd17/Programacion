country = input("Introduzca su país: ")
country = country.lower()

if country == "Argentina" or country == "argentina":
    print("\U0001F1E6 \U0001F1F7")
elif country == "España" or country == "españa":
    print("\U0001F1EA \U0001F1F8")
elif country == "Italia" or country == "italia":
    print("\U0001F1EE \U0001F1F9")
elif country == "Francia" or country == "francia":
    print("\U0001F1EB \U0001F1F7")
elif country == "Alemania" or country == "alemania":
    print("\U0001F1E9 \U0001F1EA")
elif country == "Estados Unidos" or country == "estados unidos":
    print("\U0001F1FA \U0001F1F8")
else:
    print("ERROR")
