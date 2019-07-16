import argparse
from typing import Dict


def parser() -> Dict[str, bool]:
    """
    Parse command line arguments and return pair from
    path and selection (true or false)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str,
                        help="specify path to file where image will be stored")
    parser.add_argument("-s", "--selection", action="store_true",
                        help="select area")
    args = parser.parse_args()

    return {"file": args.file,
            "selection": args.selection}
