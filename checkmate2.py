#!/usr/bin/env python

def create_matrix(board):
    list_board = list(board.replace(" ", ""))
    temp_str = "".join(list_board)
    rows_raw = temp_str.split('\n')
    
    matrix = []
    for row in rows_raw:
        if row:
            matrix.append(list(row))
            
    return matrix

def validate_rows(matrix):
    num_cols = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != num_cols:
            msg = f"❌ แถวที่ {i+1} ข้อมูลไม่ครบ! (มี {len(row)} ตัว, แต่ควรมี {num_cols} ตัว)"
            return False, msg
    return True, ""

def check_square(num_rows, num_cols):
    if num_rows == num_cols:
        print("ผลลัพธ์: เป็นตารางจัตุรัส ✅")
    else:
        print("ไม่ใช่ตารางจัตุรัส ❌")

def is_1king(board_rows):
    count = 0
    for row in board_rows:
        count += row.count('K')
    if count == 1:
        return True
    else:
        print("กรุณาใส่บอร์ดใหม่ที่มี King 1 ตัว")
        return False

def find_king(matrix): 
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'K':
                print(f"✅ เจอ King ที่ตำแหน่ง: แถว {r}, คอลัมน์ {c}")
                return r, c
    return None

# --- ฟังก์ชันหลัก ---
def checkmate2(board):
    if not board:
        print("ใส่ข้อมูล")
        return

    matrix = create_matrix(board)
    
    num_rows = len(matrix) if matrix else 0
    if num_rows == 0:
        print("ไม่มีข้อมูลแถว")
        return

    num_cols = len(matrix[0])
    print(f"Matrix ที่ได้: {matrix}")

    is_valid, error_msg = validate_rows(matrix)
    if not is_valid:
        print(error_msg)
        print("ผลลัพธ์: ไม่ใช่ตารางที่สมบูรณ์ ❌")
        return

    print(f"ขนาด: {num_rows} แถว x {num_cols} คอลัมน์")
    check_square(num_rows, num_cols)
    
    is_1king(board)
    find_king(matrix)

