from pathlib import Path
from shutil import copytree
from os import popen
from fire import Fire

def build_day(day, year='2022'):
    path = Path(str(year)) / ('day_' + str(int(day)).zfill(2))
    copytree('template', path)

    # Automatically opens directory in VSCode
    popen(f'code {str(path)}')

if __name__ == "__main__":
    Fire(build_day)
