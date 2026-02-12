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
    if not matrix: return False
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_cols:
            return False
    return True

def check_square(matrix):
    num_rows = len(matrix) if matrix else 0
    if num_rows == 0: return None, None, False
    num_cols = len(matrix[0])
    return num_rows, num_cols, num_rows == num_cols

def is_1king(matrix):
    count = 0
    for row in matrix:
        count += row.count('K')
    return count == 1

def find_king(matrix): 
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'K':
                return r, c
    return None, None



def check_Bishop(matrix, k_row, k_col):

    size = len(matrix)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for d_row, d_col in directions:
        r, c = k_row + d_row, k_col + d_col 
        while (0 <= r < size) and (0 <= c < size):
            piece = matrix[r][c]

            if piece in ('K','R','B','P','Q'):
                if piece == 'B':
                    return False 
                break
            r += d_row
            c += d_col
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
                    return False 
                break
            r += d_row
            c += d_col
    return True

def check_Pawn(matrix, k_row, k_col):
    size = len(matrix)
    directions = [(1, -1), (1, 1)] 
    
    for d_row, d_col in directions:
        r, c = k_row + d_row, k_col + d_col
        if 0 <= r < size and 0 <= c < size:
            if matrix[r][c] == 'P':
                return False  
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
                    return False 
                else:
                    break
            
            r += d_row
            c += d_col
    return True

def print_creative_board(matrix):
    print("\n--- Creative Board View ---")
    icons = {
        'K': '♔',
        'Q': '♕',
        'R': '♖',
        'B': '♗',
        'P': '♙'
    }

    for row in matrix:
        line = ""
        for char in row:
            line += icons.get(char, '⬜') + " "
        print(line)

    print("------------------------------\n")


def checkmate(board):
    if not board:
        print("Error")
        return

    matrix = create_matrix(board)

    num_rows, num_cols, is_ok = check_square(matrix)
    if not is_ok:
        print("Error")
        return
    if not check_rows(matrix):
        print("Error")
        return
    if not is_1king(matrix):
        print("Error")
        return

    print_creative_board(matrix)


    k_row, k_col = find_king(matrix)
    if k_row is None:
        print("Error")
        return

    
    if not check_Bishop(matrix, k_row, k_col):
        print("Success")
        return
    
    if not check_Rook(matrix, k_row, k_col):
        print("Success")
        return

    if not check_Pawn(matrix, k_row, k_col):
        print("Success")
        return
    
    print("Fail")