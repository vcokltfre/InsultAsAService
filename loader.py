from pathlib import Path
from json import load

def iload(filename):
    with Path("./data/" + filename + ".json").open() as f:
        return load(f)

def nload():
    with Path("./data/names.txt").open() as f:
        names = [name.strip() for name in f.readlines()]
        return names