import pygame

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

WIDTH = 50       
HEIGHT = 50      
MARGIN = 5   
BIGM = 20    
ROWS = 8         
COLS = 8         
BUTTON = 150
BCKSAMPLE = 450

SAMPLE = 1


font = pygame.font.SysFont("Arial", 20, bold=True)

# 計算視窗總大小
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
    grid.append([])          # 建立新的一列
    for column in range(COLS):
        grid[row].append(0)  # 在這一列加入 0

clock = pygame.time.Clock()
running = True
LOCK = 0
# --- 3. 遊戲主迴圈 ---
while running:
    
    # --- 事件處理 ---
    # pygame.event.get() 會回傳這段時間內發生的所有事 (滑鼠移動、按鍵盤...)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 偵測滑鼠按下事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 取得滑鼠座標
            pos = pygame.mouse.get_pos()
            
            # --- 座標轉換邏輯 ---
            # 像素座標 -> 格子索引
            # 公式：(滑鼠座標) // (格子寬 + 間距)
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            sx = (pos[0] - (WIDTH + MARGIN) * COLS - MARGIN - BIGM) // (WIDTH + MARGIN)
            sy = pos[1] // (HEIGHT + MARGIN)
            # 為了防止點到邊界外報錯，加一個檢查
            if 0 <= row < ROWS and 0 <= column < COLS and LOCK == 0:
                # --- 切換狀態邏輯 ---
                # 如果是 0 變 1，如果是 1 變 0
                if grid[row][column] == 0:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0

            
            elif lockbotx <= pos[0] < lockbotx + LOCKBOTWIDTH and lockboty <= pos[1] < lockboty + HEIGHT:
                LOCK = (LOCK + 1) % 2
            '''
            elif 0 < sx <= 5 and sy == 0:
                SAMPLE = sx
            '''



    # --- 繪圖處理 ---
    screen.fill(WHITE) # 清空背景

    # 雙層迴圈把 8x8 的格子畫出來
    for row in range(ROWS):
        for column in range(COLS):
            # 決定顏色：根據 grid[row][column] 的值
            mouse_pos = pygame.mouse.get_pos()
            hover_col = mouse_pos[0] // (WIDTH + MARGIN)
            hover_row = mouse_pos[1] // (HEIGHT + MARGIN)
            if grid[row][column] == 1:
                color = RED
                if row == hover_row and column == hover_col:
                    color = LRED
            elif row == hover_row and column == hover_col:
                color = LGRAY
            else :
                color = GRAY
            # 計算矩形要在螢幕上的位置
            rect_x = (MARGIN + WIDTH) * column + MARGIN
            rect_y = (MARGIN + HEIGHT) * row + MARGIN
            
            # 畫出矩形
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
    # 取得文字的矩形外框，並設定它的中心點 = 按鈕的中心點
    text_rect = text_surface.get_rect(center=bot_rect.center)
    
    # 貼上文字
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
    for i in range(1,4):
        for j in range(1,4):
            srect_x = (MARGIN + WIDTH) * (COLS + i) + MARGIN + BIGM
            srect_y = (MARGIN + WIDTH) * (j) + MARGIN 
            s_rect = pygame.Rect(srect_x, srect_y, WIDTH, HEIGHT)
            scolor = GRAY
            pygame.draw.rect(screen, color, s_rect)
            
            
    # 更新畫面
    pygame.display.flip()
    clock.tick(60)

pygame.quit()