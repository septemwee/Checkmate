#!/usr/bin/env python
from checkmate import checkmate

def main():
    board = """\
....
....
..B.
.K..\
    """
    checkmate(board)

if __name__ == "__main__":
    main()
