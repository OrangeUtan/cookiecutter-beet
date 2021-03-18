import os
from pathlib import Path

def is_file_empty(file: Path):
    return os.stat(file).st_size == 0

def remove_empty_files():

    root = Path(os.getcwd())
    for dirpath, _, filenames in os.walk(root):
        for file in [Path(dirpath, f) for f in filenames]:
            if is_file_empty(file):
                os.remove(file)

if __name__ == "__main__":
    remove_empty_files()