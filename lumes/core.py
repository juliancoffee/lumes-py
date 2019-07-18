import subprocess
import sys
from typing import List


def screenshot(selection: bool) -> bytes:
    """
    Get boolean selection,
    take a screenshot and return it as bytes
    """
    cmd = ["maim"]
    if selection:
        cmd.append("-s")

    try:
        img = subprocess.run(cmd, stdout=subprocess.PIPE).stdout
    except FileNotFoundError:
        sys.stderr.write("We can't find {} in your $PATH\n".format(cmd[0]))
        sys.exit(1)

    return img


def to_clipboard(img: bytes) -> None:
    """
    Take image from arguments (bytes returned from function screenshot)
    and place it to clipboard using xclip
    """
    cmd = ["xclip", "-selection", "clipboard", "-t", "image/png"]
    try:
        subprocess.run(cmd, input=img)
    except FileNotFoundError:
        sys.stderr.write("We can't find {} in your $PATH\n".format(cmd[0]))
        sys.exit(1)


def to_save(img: bytes, path: str) -> None:
    """
    Save file (bytes returned from screenshot) to given path
    """
    with open(path, mode='wb') as temp:
        temp.write(img)
