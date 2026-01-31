# solver.py
def turn_b_to_r(g) :
    for i in range(0,8) :
        for j in range(0,8):
            if g[i][j] == 2 :
                g[i][j] = 1
    return

def reset(g) :
    for i in range(0,8) :
        for j in range(0,8):
                g[i][j] = 0
    return


def get_shape_coords(block_3x3):
    """ 將 3x3 矩陣轉為相對座標 """
    coords = []
    for r in range(3):
        for c in range(3):
            if block_3x3[r][c] == 1:
                coords.append((r, c))
    
    if not coords:
        return []

    min_r = min(p[0] for p in coords)
    min_c = min(p[1] for p in coords)
    return [(r - min_r, c - min_c) for r, c in coords]

def can_place(grid, shape_coords, r, c):
    """ 檢查是否可放置 """
    rows = len(grid)
    cols = len(grid[0])
    for dr, dc in shape_coords:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False
        if grid[nr][nc] == 1:
            return False
    return True


def find_first_solution(grid, samples):
    """
    修改版：會依序檢查 3 個樣本框 (index 0, 1, 2)
    只要找到任何一個能放進去的，就立刻回傳。
    """
    # 遍歷 samples 裡面的每一個方塊 (idx 是 0, 1, 2)
    for idx, block in enumerate(samples):
        shape_coords = get_shape_coords(block)
        
        # 如果這個方塊是空的，就跳過，檢查下一個
        if not shape_coords:
            continue
            
        # 拿著這個方塊，掃描 8x8 盤面
        for r in range(8):
            for c in range(8):
                if can_place(grid, shape_coords, r, c):
                    # 找到解了！
                    return (idx, r, c, shape_coords)
    return None # 全部都試過了，沒一個能放