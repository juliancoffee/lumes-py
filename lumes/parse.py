import argparse
from typing import Dict, Union


def parser() -> Dict[str, Union[str, bool]]:
    """
    Parse command line arguments and return pair from
    path and selection (true or false)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str,
                        help="specify path to catalog, where screenshots will be stored")
    parser.add_argument("-f", "--file", type=str,
                        help="specify path to file where image will be stored")
    parser.add_argument("-s", "--selection", action="store_true",
                        help="use this flag if you want to select area")
    args = parser.parse_args()

    return {"file": args.file,
            "dir": args.directory,
            "selection": args.selection}
