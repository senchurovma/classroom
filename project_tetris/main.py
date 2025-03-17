import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10 # 20 строк и 10 столбцов
CELL_SIZE = WIDTH // COLS
FPS = 60

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# тетромино в виде матриц
SHAPES = [
    [[1, 1, 1, 1]],         # I
    [[1, 0, 0], [1, 1, 1]], # J
    [[0, 0, 1], [1, 1, 1]], # L
    [[1, 1], [1, 1]],       # O
    [[0, 1, 1], [1, 1, 0]], # S
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 1, 0], [0, 1, 1]]  # Z
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tetris")
clock = pygame.time.Clock() # для контроля фпс

pygame.mixer.music.load("C:/Users/mishk/Documents/vscode_inf/classroom/project_tetris/tetris_theme.ogg")
pygame.mixer.music.play(-1) # фоновая музыка проигрывается в цикле

background = pygame.image.load("C:/Users/mishk/Documents/vscode_inf/classroom/project_tetris/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) # подгоняем масштаб

grid = [[0 for i in range(COLS)] for i in range(ROWS)] # заполняем двумерный список пустыми клетками

score = 0
font = pygame.font.Font("C:/Users/mishk/Documents/vscode_inf/classroom/project_tetris/alagard.ttf", 24)

record_file = "highscore.txt"
if not os.path.exists(record_file):
    with open(record_file, "w") as f:
        f.write("0")

with open(record_file, "r") as f:
    highscore = int(f.read())

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2 # от центра игрового поля отступаем на половину от ширины первой строчки фигуры (в клетках)
        self.y = 0

    def rotate(self): # вращает фигуру на 90 градусов по часовой стрелке
        self.shape = [list(row) for row in zip(*self.shape[::-1])] # отражаем матрицу по горизонтали, затем транспонируем и превращаем кортежи в списки

    def valid(self, dx=0, dy=0): # по умолчанию проверка выполяется для текущего положения фигуры
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell: # i и j - смещение относительно верхнего левого угла фигуры
                    nx, ny = self.x + j + dx, self.y + i + dy # новые координаты
                    if nx < 0 or nx >= COLS or ny >= ROWS or (ny >= 0 and grid[ny][nx]):
                        return False # в этом случае перемещение или поворот невозможны
        return True

    def place(self): # фиксируем фигуру в сетке
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    grid[self.y + i][self.x + j] = self.color

def clear_lines():
    global grid, score, fall_speed, highscore
    lines_cleared = 0
    grid = [row for row in grid if any(cell == 0 for cell in row)] # в новую сетку попадают только незаполненные строки,  or not row.count(0) == 0
    while len(grid) < ROWS: # почистили, теперь добавляем новые строки сверху
        grid.insert(0, [0 for i in range(COLS)]) # строка - список путсых ячеек
        lines_cleared += 1 # награда
    score += lines_cleared * 100

    if score > highscore:
        highscore = score
        with open(record_file, "w") as f:
            f.write(str(highscore))

    if score > 0 and score % 500 == 0:
        fall_speed = max(0.1, fall_speed - 0.05)

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = grid[y][x] if grid[y][x] else GRAY # если ячейка содержит цвет, его и используем
            pygame.draw.rect(screen, color, rect, 0 if grid[y][x] else 1) # рисует прямоугольник на экране игры

def draw_tetromino(tetromino):
    for i, row in enumerate(tetromino.shape):
        for j, cell in enumerate(row):
            if cell:
                rect = pygame.Rect((tetromino.x + j) * CELL_SIZE, (tetromino.y + i) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, tetromino.color, rect)

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE) # true отвечает за сглаживание
    screen.blit(score_text, (10, 10)) # рендеринг поверх основного экрана
    record_text = font.render(f"Highscore: {highscore}", True, WHITE)
    screen.blit(record_text, (10, 40))

fall_time = 0
fall_speed = 0.5
tetromino = Tetromino()
running = True
while running: # основной игровой цикл
    dt = clock.tick(FPS) / 1000 # ограничиваем фпс
    fall_time += dt # dt - время, прошедшее с предыдущего кадра

    for event in pygame.event.get(): # обработка событий
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and tetromino.valid(dx=-1):
                tetromino.x -= 1
            elif event.key == pygame.K_RIGHT and tetromino.valid(dx=1):
                tetromino.x += 1
            elif event.key == pygame.K_DOWN and tetromino.valid(dy=1):
                tetromino.y += 1
            elif event.key == pygame.K_UP:
                previous_shape = tetromino.shape.copy() # на случай, если поворот невозможен
                tetromino.rotate()
                if not tetromino.valid():
                    tetromino.shape = previous_shape

    if fall_time > fall_speed: # падение фигуры за счет перемещения на клетку вниз
        if tetromino.valid(dy=1):
            tetromino.y += 1
        else:
            tetromino.place()
            clear_lines()
            tetromino = Tetromino()
            if not tetromino.valid():
                print("Конец игры")
                running = False
        fall_time = 0

    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    draw_grid()
    draw_tetromino(tetromino)
    draw_score()
    pygame.display.flip()

pygame.quit()