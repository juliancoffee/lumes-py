from .core import *
from .parse import parser
from .save import save_path

def main():
    args = parser()

    selection = args["selection"]
    img = screenshot(selection)

    to_clipboard(img)
    print("Screenshot saved to clipboard")

    if args["file"]:
        path = args["file"]
    elif args["dir"]:
        ext = ".png"
        path = save_path(args["dir"], ext)
    else:
        path = ''

    if path:
        to_save(img, path)
        print("File saved to {}".format(path))

if __name__ == "__main__":
    main()

