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

