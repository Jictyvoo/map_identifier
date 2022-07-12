import typing
from os.path import join
from pathlib import Path


class FileSaverRepository:
    def save_file(self, path: str, filename: str, content: typing.Any):
        Path(path).mkdir(parents=True, exist_ok=True)
        filepath = join(path, filename)
        print("Saving file to %s" % filepath)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        return filepath
