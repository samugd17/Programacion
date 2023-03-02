# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = []
    with open(datafile) as f:
        keys = f.readline().strip().split(",")
        for line in f:
            pokemon_stats = line.strip().split(",")
            for stat in pokemon_stats:  
                if stat.isnumeric():
                    stat_index = pokemon_stats.index(stat)
                    pokemon_stats[stat_index] = int(stat)
                if stat == "False":
                    stat_index = pokemon_stats.index(stat)
                    pokemon_stats[stat_index] = False
            stats = dict(zip(keys, pokemon_stats))
            data.append(stats)

    return data


if __name__ == "__main__":
    run("data/read_csv/pokemon.csv")
