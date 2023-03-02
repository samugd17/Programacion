# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    fitems = {}
    for item, value in items.items():
        fitems[item.replace(" ", "")] = value

    return fitems


if __name__ == "__main__":
    run({"S  001": ["Math", "Science"], "S    002": ["Math", "English"]})
