from os import listdir
from datetime import datetime


def save_path(save_dir: str, ext: str) -> str:
    t = datetime.now()
    save_file = "{y}|{mth}|{d}_{h}:{mn}:{s}".format(
        y=t.year,
        mth=t.month,
        d=t.day,
        h=t.hour,
        mn=t.minute,
        s=t.second,
    )
    
    # check if file won't have duplicates
    ls = listdir(save_dir)
    while (save_file + ext) in ls:
        save_file += "_1"
    return save_file + ext
