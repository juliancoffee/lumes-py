import subprocess
from typing import List


def screenshot(selection: bool) -> bytes:
    """
    Get boolean selection,
    take a screenshot and return it as bytes
    """
    if selection:
        img = subprocess.run(["maim", "-s"], stdout=subprocess.PIPE).stdout
    else:
        img = subprocess.run(["maim"], stdout=subprocess.PIPE).stdout
    return img


def to_clipboard(img: bytes) -> None:
    """
    Take image from arguments (bytes returned from function screenshot)
    and place it to clipboard using xclip
    """
    clip = subprocess.run(
                ["xclip",
                    "-selection", "clipboard",
                    "-t", "image/png"],
                input=img)


def to_save(img: bytes, path: str) -> None:
    """
    Save file (bytes returned from screenshot) to given path
    """
    with open(path, mode='wb') as temp:
        temp.write(img)
