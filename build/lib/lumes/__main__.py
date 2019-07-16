from .core import *
from .parse import parser

def main():
    #TODO implement save to path
    #path = args["path"]

    args = parser()
    path = args["file"]
    selection = args["selection"]
    img = screenshot(selection)
    clip_board(img)
    if path:
        save_file(img, path)

if __name__ == "__main__":
    main()

