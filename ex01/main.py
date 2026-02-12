#!/usr/bin/env python
import sys
import os
from checkmate import checkmate

def main():
    board = """\
    # . . K
    . . P .
    . . . .
    . . . .\
    """
    checkmate(board)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main()
    else:
        for filename in sys.argv[1:]:
            if os.path.exists(filename):
                try:
                    with open(filename, 'r') as f:
                        board_content = f.read()
                        checkmate(board_content)
                except Exception as e:
                    print("Error")
            else:
                print(f"Error: File {filename} not found")