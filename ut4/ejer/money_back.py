# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    # money_back = {}
    # available_currencies = sorted(available_currencies, reverse=True)
    # rest_money = to_give_back
    # for currency in available_currencies:
    #     counter_currency = 0
    #     while rest_money - currency >=0:
    #         rest_money -= currency
    #         counter_currency +=1
    #         money_back[currency]=counter_currency
    # if rest_money == 0:
    #     return money_back
    # else:
    #     return None

    money_back = {}
    for currency in sorted(available_currencies, reverse=True):
        if to_give_back > 0:
            currency_qty = to_give_back // currency
            to_give_back %= currency
            money_back[currency] = currency_qty
        else:
            return money_back
    return None



if __name__ == "__main__":
    run(20, [5, 2, 1])
