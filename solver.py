DELETE = 10
SAMPLE1 = 11
SAMPLE2 = 12
SAMPLE3 = 13
TEMP = 1001

def turn_b_to_r(g) :
    for i in range(0,8) :
        for j in range(0,8):
            if g[i][j] != 0 :
                g[i][j] = 1
    return

def reset(g) :
    for i in range(0,8) :
        for j in range(0,8):
                g[i][j] = 0
    return

def del_if_line(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows - 1, -1, -1):
        if 0 not in grid[i]: 
            for j in range(0,cols):
                grid[i][j] = DELETE

    for i in range(cols - 1, -1, -1):
        check = False
        for j in range(rows - 1, -1, -1):
            if grid[j][i] == 0 :
                check = True
        if check == False:
            for j in range(rows - 1, -1, -1):
                grid[j][i] = DELETE

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if grid[i][j] == DELETE:
                grid[i][j] = 0


def get_shape_coords(sample):
    coords = []
    for r in range(3):
        for c in range(3):
            if sample[r][c] == 1:
                coords.append((r, c))
    
    if not coords:
        return []

    min_r = min(p[0] for p in coords)
    min_c = min(p[1] for p in coords)
    return [(r - min_r, c - min_c) for r, c in coords]

def can_place(grid, shape_coords, r, c):
    rows = len(grid)
    cols = len(grid[0])
    for dr, dc in shape_coords:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False
        if grid[nr][nc] == 1:
            return False
    return True


def find_solution(grid, samples):
    for idx, block in enumerate(samples):
        shape_coords = get_shape_coords(block)
        
        if not shape_coords:
            continue
            
        for r in range(8):
            for c in range(8):
                if can_place(grid, shape_coords, r, c):
                    return (idx, r, c, shape_coords)
    return None 

'''def find_final_sol(grid, samples, active_indices,ans,allsol):
    for i, block in enumerate(samples):
        shape_coords = get_shape_coords(block)
        if get_shape_coords(block) and (i not in active_indices):
            active_indices.append(i)
            for r in range(8):
                for c in range(8):
                    if can_place(grid, shape_coords, r, c):
                        ans.append(i, r, c, shape_coords)
                        find_final_sol(grid, samples, active_indices,ans,allsol)
                        if len(active_indices) == 3:
                            allsol.append(ans)
                        
    return 

def sol(grid,samples):
    active_indices = []
    ans = []
    allsol = []
    for i, block in enumerate(samples):
        if get_shape_coords(block):
            active_indices.append(i)
    return find_final_sol(grid, samples, active_indices,ans,allsol)

'''

# 這是你原本有的 helper function，我假設它們已經寫好了
# from solver import get_shape_coords, can_place, del_if_line

def sol(grid, samples):
    todo_indices = [] 
    for i, block in enumerate(samples):
        if get_shape_coords(block):
            todo_indices.append(i)
    return find_final_sol(grid, samples, todo_indices)

def find_final_sol(current_grid, samples, remaining_indices):
    if not remaining_indices:
        return [] 

    for idx in remaining_indices:
        shape_coords = get_shape_coords(samples[idx])
        for r in range(8):
            for c in range(8):
                if can_place(current_grid, shape_coords, r, c):
                    next_grid = [row[:] for row in current_grid]
                    
                    for dr, dc in shape_coords:
                        next_grid[r + dr][c + dc] = 1
                    del_if_line(next_grid)
                    next_remaining = [x for x in remaining_indices if x != idx]
                    
                    result_path = find_final_sol(next_grid, samples, next_remaining)
                    
                    if result_path is not None:
                        current_move = (idx, r, c, shape_coords)
                        return [current_move] + result_path
    
    return None

    


    

