#!/usr/bin/env python
from checkmate2 import checkmate2

def main():
    board = """\
    # # . .
    K . P .
    . K . .
    . . . .\
    """
    checkmate2(board)

if __name__ == "__main__":
    main()
