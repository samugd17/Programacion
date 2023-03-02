# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    cities = {}
    for city in cinfo.split(";"):
        pre_keyword = city.split(":")
        keyword = pre_keyword[0]
        argument = int(pre_keyword[1])
        cities[keyword] = argument

    return cities


if __name__ == "__main__":
    run("Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000")
