# def vending(num_article, money):
num_article = 1
money = 1
article_code = []
price = []
stock = []
articles_info = {"KitKat": [1, 0.9, 5], "Mars": [2, 0.80, 6], "Fanta": [3, 1.20, 4]}

for article_data in articles_info.values():
    article_code.append(article_data[0])
    price.append(article_data[1])
    stock.append(article_data[2])
for code in article_code:
    if num_article not in article_code:
        print("No existe ese producto")
        break
    elif money < price[num_article]:
        print("Dinero insuficiente")
        break
    else:
        remaining_money = money - price[num_article]
        stock[num_article] -= 1
        print(remaining_money)


# stock
