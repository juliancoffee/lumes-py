from .core import *
from .parse import parser

from typing import Dict

def main(args: Dict[str, bool]):
    #TODO implement save to path
    #path = args["path"]
    path = args["file"]
    selection = args["selection"]
    img = screenshot(selection)
    clip_board(img)
    if path:
        save_file(img, path)

if __name__ == "__main__":
    args = parser()
    main(args)

