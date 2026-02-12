<<<<<<< Updated upstream
=======
#!/usr/bin/env python
import sys
import os

def create_matrix(board):
    list_board = list(board.replace(" ", ""))
    temp_str = "".join(list_board)
    rows_raw = temp_str.split('\n')
    
    matrix = []
    for row in rows_raw:
        if row:
            matrix.append(list(row))
            
    return matrix

def check_rows(matrix):
    num_cols = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != num_cols:
            # print(f"กรุณาป้อนกระดานให้สมบูรณ์")
            return False
    return True

    
def check_square(matrix):
    num_rows = len(matrix) if matrix else 0
    
    if num_rows == 0:
        # print("ไม่มีข้อมูลแถว")
        return None, None, False

    num_cols = len(matrix[0])
    
    # print(f"Matrix ที่ได้: {matrix}")

    if num_rows == num_cols:
        return num_rows, num_cols, True
    else:
        # print("กรุณาป้อนกระดานขนาดจัตุรัส")
        return num_rows, num_cols, False

def is_1king(matrix):
    count = 0
    for row in matrix:
        count += row.count('K')
    if count == 1:
        return True
    else:
        # print("กรุณาป้อน King 1 ตัวเท่านั้น")
        return False

def find_king(matrix): 
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'K':
                # print(f"เจอ King ที่ตำแหน่ง: แถว {r}, คอลัมน์ {c}")
                return r, c
    return None,None


def check_Bishop(matrix, k_row, k_col):
    size = len(matrix)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for d_row, d_col in directions:
        r, c = k_row + d_row, k_col + d_col 
        
        while (0 <= r < size) and (0 <= c < size):
            piece = matrix[r][c]
            if piece in ('K','R','B','P','Q'):
                if piece == 'B':
                    # print("Success")
                    return False
                break
            r += d_row
            c += d_col

    # print("Bishop: FAIL")     
    return True

def check_Rook(matrix, k_row, k_col):
    size = len(matrix)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
     
    for d_row, d_col in directions:
        r, c = k_row + d_row, k_col + d_col 
        
        while (0 <= r < size) and (0 <= c < size):
            piece = matrix[r][c]
            
            if piece in ('K','R','B','P','Q'):
                if piece == 'R':
                    # print("Success")
                    return False
                break
            r += d_row
            c += d_col
    # print("Rook: FAIL")     
    return True

def check_Pawn(matrix, k_row, k_col):
    
    size = len(matrix)
    attack_positions = [(1, -1), (1, 1)] 
    
    for d_row, d_col in attack_positions:
        r, c = k_row + d_row, k_col + d_col
        
        if 0 <= r < size and 0 <= c < size:
            if matrix[r][c] == 'P':
                # print("Success")
                return False  
                
    # print("Pawn: FAIL")
    return True 

def check_Queen(matrix, k_row, k_col):
    size = len(matrix)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    
    for d_row, d_col in directions:
        r, c = k_row + d_row, k_col + d_col
        
        while (0 <= r < size) and (0 <= c < size):
            piece = matrix[r][c]
            
            if piece in ('K', 'R', 'B', 'Q', 'P'):
                if piece == 'Q':
                    # print("Success")
                    return False 
                else:
                    break
            
            r += d_row
            c += d_col
            
    # print("Queen: FAIL")
    return True
    

>>>>>>> Stashed changes
def checkmate(board):
    # 1. แปลงสตริงกระดานให้เป็น List 2 มิติ (Matrix) เพื่อให้ดูง่าย
    # กำจัดช่องว่างส่วนเกินและแยกบรรทัด
    rows = [line.strip() for line in board.strip().split('\n')]
    size = len(rows)
    
    # 2. หาตำแหน่งของ King (K)
    king_pos = None
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                break
    
    if not king_pos:
        return # หากไม่พบ King ให้คืนการควบคุมตามโจทย์ 

    kr, kc = king_pos

    # 3. ตัวอย่างการเช็คทิศทาง (เช่น เช็คแนวตรงสำหรับ Rook และ Queen)
    # เราจะเช็ค 4 ทิศ: บน, ล่าง, ซ้าย, ขวา
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        curr_r, curr_c = kr + dr, kc + dc
        while 0 <= curr_r < size and 0 <= curr_c < size:
            piece = rows[curr_r][curr_c]
            if piece != '.': # ถ้าเจอตัวหมาก [cite: 22, 25]
                if piece in ('R', 'Q'): # ถ้าเป็นตัวที่เดินแนวตรงได้ 
                    print("Success")
                    return
                break # เจอตัวอื่นขวาง ให้หยุดเช็คทิศนี้ [cite: 22]
            curr_r += dr
            curr_c += dc

    # 4. (คุณต้องเขียนเพิ่ม: เช็คแนวทแยงสำหรับ Bishop, Queen และเช็ค Pawn)
    # ...
    
    print("Fail") # ถ้าเช็คครบทุกอย่างแล้วไม่โดนรุก