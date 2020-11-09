from pathlib import Path
from json import load

def iload(filename):
    with Path("./data/" + filename + ".json").open() as f:
        return load(f)