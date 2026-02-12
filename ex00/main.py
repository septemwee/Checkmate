#!/usr/bin/env python
from checkmate import checkmate

def main():
    board = """\
    # # . .
    . . . .
    . K . .
    P . . .\
    """
    checkmate(board)

if __name__ == "__main__":
    main()
