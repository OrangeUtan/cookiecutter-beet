import os
from pathlib import Path
import shutil

def is_file_empty(file: Path):
    return os.stat(file).st_size == 0

def remove_empty_files(root: Path):
    for dirpath, _, filenames in os.walk(root):
        for file in [Path(dirpath, f) for f in filenames]:
            if is_file_empty(file):
                os.remove(file)

if __name__ == "__main__":
    root = Path(os.getcwd())

    remove_empty_files(root)

    if not "{{cookiecutter.datapack}}" == "y":
        shutil.rmtree(Path(root, "datapack"))
    if not "{{cookiecutter.resourcepack}}" == "y":
        shutil.rmtree(Path(root, "resourcepack"))