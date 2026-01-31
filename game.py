import pygame
import solver

pygame.init()

WHITE = (255, 255, 255)  
GRAY  = (200, 200, 200)  
RED   = (255, 50, 50) 
LRED  = (255,100,0)  
LGRAY = (225, 225, 225) 
FORUMGOLD = (255, 227, 132)
BANANA = (227,207,87)
BLACK = (0, 0, 0)
DOUGELLO = (235,142,85)
BLUE = (0,0,255)

WIDTH = 50       
HEIGHT = 50      
MARGIN = 5   
BIGM = 20    
ROWS = 8         
COLS = 8         
BUTTON = 200
BCKSAMPLE = 450

SAMPLE = 1


font = pygame.font.SysFont("Arial", 20, bold=True)

#window
WINDOW_SIZE = [
    (WIDTH + MARGIN) * COLS + MARGIN + BCKSAMPLE,
    (HEIGHT + MARGIN) * ROWS + MARGIN + BUTTON
]

lockbotx = (MARGIN + WIDTH) * (COLS - 2) + MARGIN
lockboty = (MARGIN + WIDTH) * ROWS + MARGIN 
LOCKBOTWIDTH = WIDTH * 2 + MARGIN

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("8x8 格子狀態切換測試")

grid = []
for row in range(ROWS):
    grid.append([])          
    for column in range(COLS):
        grid[row].append(0)  

sample_data = [[[0]*3 for _ in range(3)] for _ in range(3)]



clock = pygame.time.Clock()
running = True
LOCK = 0
#main
while running:
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            sx = (pos[0] - (WIDTH + MARGIN) * COLS - MARGIN - BIGM) // (WIDTH + MARGIN)
            sy = pos[1] // (HEIGHT + MARGIN)
            if 0 <= row < ROWS and 0 <= column < COLS and LOCK == 0:
                if grid[row][column] == 0:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0

            
            elif lockbotx <= pos[0] < lockbotx + LOCKBOTWIDTH and lockboty <= pos[1] < lockboty + HEIGHT:
                LOCK = (LOCK + 1) % 2
            elif 1 <= sx <= 3 and LOCK == 0:
                s_col = sx - 1  
                target_s = -1  
                s_row = -1     

                if 0 <= sy <= 2:     
                    target_s, s_row = 0, sy
                elif 4 <= sy <= 6:   
                    target_s, s_row = 1, sy - 4
                elif 8 <= sy <= 10:   
                    target_s, s_row = 2, sy - 8
                
                if target_s != -1:
                    sample_data[target_s][s_row][s_col] = 1 - sample_data[target_s][s_row][s_col]
            '''
            elif 0 < sx <= 5 and sy == 0:
                SAMPLE = sx
            '''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                 solver.reset(grid)

            elif event.key == pygame.K_SPACE: 
                solver.turn_b_to_r(grid)

                counts = []
                for s in sample_data:
                    count = sum(sum(row) for row in s)
                    counts.append(count)
            
                result = solver.find_first_solution(grid, sample_data)
            
                if result:
                    idx, r, c, shape = result
                
                    for dr, dc in shape:
                        grid[r + dr][c + dc] = 2 
                else:
                    print("fail")
        

    screen.fill(WHITE) 
    #deal hover and color
    for row in range(ROWS):
        for column in range(COLS):
            mouse_pos = pygame.mouse.get_pos()
            hover_col = mouse_pos[0] // (WIDTH + MARGIN)
            hover_row = mouse_pos[1] // (HEIGHT + MARGIN)
            if grid[row][column] == 1:
                color = RED
                if row == hover_row and column == hover_col:
                    color = LRED
            elif grid[row][column] == 2:
                color = BLUE
            elif row == hover_row and column == hover_col:
                color = LGRAY
            else :
                color = GRAY
            
            rect_x = (MARGIN + WIDTH) * column + MARGIN
            rect_y = (MARGIN + HEIGHT) * row + MARGIN
            
            
            pygame.draw.rect(screen, color, [rect_x, rect_y, WIDTH, HEIGHT])
    #draw botton for lock
    mouse_pos = pygame.mouse.get_pos()
    if lockbotx <= mouse_pos[0] < lockbotx + LOCKBOTWIDTH and lockboty <= mouse_pos[1] < lockboty + HEIGHT:
        botcolor = BANANA
    else :
        botcolor = FORUMGOLD
    lockbotx = (MARGIN + WIDTH) * (COLS - 2) + MARGIN
    lockboty = (MARGIN + WIDTH) * ROWS + MARGIN 
    LOCKBOTWIDTH = WIDTH * 2 + MARGIN
    bot_rect = pygame.Rect(lockbotx, lockboty, LOCKBOTWIDTH, HEIGHT)
    pygame.draw.rect(screen, botcolor, bot_rect)
    if LOCK == 0:
        text_surface = font.render("LOCK", True, BLACK) 
    else :
        text_surface = font.render("UNLOCK", True, BLACK) 
    text_rect = text_surface.get_rect(center=bot_rect.center)
    screen.blit(text_surface, text_rect)

    #sample
    '''
    for i in range(1,6):
        srect_x = (MARGIN + WIDTH) * (COLS + i) + MARGIN + BIGM
        srect_y = MARGIN
        s_rect = pygame.Rect(srect_x, srect_y, WIDTH, HEIGHT)
        scolor = FORUMGOLD
        if i == SAMPLE:
            scolor = DOUGELLO
        pygame.draw.rect(screen, scolor, s_rect)
        text_surface = font.render(str(i), True, BLACK) 
        text_rect = text_surface.get_rect(center=s_rect.center)
        screen.blit(text_surface, text_rect)
    match SAMPLE:
        case 1:
            print(1)
        case 2: 
            print(2)
    '''

    mpos = pygame.mouse.get_pos()
    msx = (mpos[0] - (WIDTH + MARGIN) * COLS - MARGIN - BIGM) // (WIDTH + MARGIN)
    msy = mpos[1] // (HEIGHT + MARGIN)

    offsets = [0, 3, 7] 

    for k in range(3): 
        for i in range(1, 4):
            for j in range(1, 4):
                visual_y_offset = j + offsets[k] 
                if k == 0: visual_y_offset = j-1 
                
                srect_x = (MARGIN + WIDTH) * (COLS + i) + MARGIN + BIGM
                srect_y = (MARGIN + WIDTH) * visual_y_offset + MARGIN 
                
                if k == 0: srect_y = (MARGIN + WIDTH) * (j-1) + MARGIN
                
                s_rect = pygame.Rect(srect_x, srect_y, WIDTH, HEIGHT)
                
                is_on = sample_data[k][j-1][i-1] == 1
                
                check_y = j-1 if k==0 else (j+3 if k==1 else j+7)
                is_hover = (msx == i and msy == check_y)

                if is_on:
                    scolor = LRED if is_hover else RED
                else:
                    scolor = LGRAY if is_hover else GRAY

                pygame.draw.rect(screen, scolor, s_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()