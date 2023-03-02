# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
   
    money_back = {}
    for currency, max_currency_qty in sorted(available_currencies.items(), reverse=True):
        currency_qty_ = to_give_back // currency
        currency_qty = min(max_currency_qty)
    return None


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})