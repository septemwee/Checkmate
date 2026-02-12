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