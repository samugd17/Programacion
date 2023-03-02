# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = "data/txt2md/outline.md"
    lines = []
    with open(text_path) as f:
        for line in f:
            tab = line.count("\t") + 1
            line = "#" * tab + " " + line.strip("\t").strip()
            lines.append(line)
    with open(md_path, "w") as f:
        for line in lines:
            f.write(f"{line}\n")

    return filecmp.cmp(md_path, "data/txt2md/.expected", shallow=False)


if __name__ == "__main__":
    run("data/txt2md/outline.txt")
