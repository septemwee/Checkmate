#!/usr/bin/env python
import sys
import os
from checkmate import checkmate

def main():
    # บอร์ดตัวอย่างสำหรับการรันเทสเอง
    board = """\
. K . .
. . P .
. . . .
. . . ."""
    checkmate(board)

if __name__ == "__main__":
    # ตรวจสอบว่ามีชื่อไฟล์ส่งมาไหม
    if len(sys.argv) < 2:
        main()
    else:
        # วนลูปอ่านไฟล์ทีละไฟล์
        for filename in sys.argv[1:]:
            # print(f"Checking file: {filename}") 
            if os.path.exists(filename):
                try:
                    with open(filename, 'r') as f:
                        board_content = f.read()
                        checkmate(board_content)
                except Exception as e:
                    print("Error")
            else:
                print(f"Error: File {filename} not found")