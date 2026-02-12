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
                    print("Success")
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
                    print("Success")
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
                print("Success")
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
                    print("Success")
                    return False 
                else:
                    break
            
            r += d_row
            c += d_col
            
    # print("Queen: FAIL")
    return True

def checkmate(board):
    if not board:
        # print("กรุณาใส่ข้อมูล")
        return

    matrix = create_matrix(board)
    
    
    num_rows, num_cols, is_ok = check_square(matrix)
    # print(f"ขนาด: {num_rows} แถว x {num_cols} คอลัมน์")
    if not is_ok:
        return
    
    if not check_rows(matrix):
        return
    
    if not is_1king(matrix):
        return

    k_row,k_col = find_king(matrix)
    if k_row is None or k_col is None:
        return


    if not check_Bishop(matrix,k_row,k_col):
        return
    
    if not check_Rook(matrix,k_row,k_col):
        return

    if not check_Pawn(matrix, k_row, k_col):
        return

    if not check_Queen(matrix, k_row, k_col):
        return
    

    print("Fail")



