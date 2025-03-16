import pygame
import random
import os

# Инициализация
pygame.init()

# Константы
WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10
CELL_SIZE = WIDTH // COLS
FPS = 60

# Цвета
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

# Фигуры
SHAPES = [
    [[1, 1, 1, 1]], 
    [[1, 0, 0], [1, 1, 1]], 
    [[0, 0, 1], [1, 1, 1]], 
    [[1, 1], [1, 1]], 
    [[0, 1, 1], [1, 1, 0]], 
    [[0, 1, 0], [1, 1, 1]], 
    [[1, 1, 0], [0, 1, 1]]
]

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tetris")
clock = pygame.time.Clock()

# Загрузка музыки
pygame.mixer.music.load("C:/Users/mishk/Documents/vscode_inf/classroom/project_tetris/tetris_theme.ogg")
pygame.mixer.music.play(-1)

# Загрузка фона
background = pygame.image.load("C:/Users/mishk/Documents/vscode_inf/classroom/project_tetris/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Подгонка изображения под размер экрана

# Сетка
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Счет
score = 0
font = pygame.font.Font("C:/Users/mishk/Documents/vscode_inf/classroom/project_tetris/alagard.ttf", 24)

# Рекорд
record_file = "highscore.txt"
if not os.path.exists(record_file):
    with open(record_file, "w") as f:
        f.write("0")

with open(record_file, "r") as f:
    highscore = int(f.read())

# Класс фигуры
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def valid(self, dx=0, dy=0):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    nx, ny = self.x + j + dx, self.y + i + dy
                    if nx < 0 or nx >= COLS or ny >= ROWS or (ny >= 0 and grid[ny][nx]):
                        return False
        return True

    def place(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    grid[self.y + i][self.x + j] = self.color

# Очистка линий
def clear_lines():
    global grid, score, fall_speed, highscore
    lines_cleared = 0
    grid = [row for row in grid if any(cell == 0 for cell in row) or not row.count(0) == 0]
    while len(grid) < ROWS:
        grid.insert(0, [0 for _ in range(COLS)])
        lines_cleared += 1
    score += lines_cleared * 100

    if score > highscore:
        highscore = score
        with open(record_file, "w") as f:
            f.write(str(highscore))

    if score > 0 and score % 500 == 0:
        fall_speed = max(0.1, fall_speed - 0.05)

# Отрисовка
def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = grid[y][x] if grid[y][x] else GRAY
            pygame.draw.rect(screen, color, rect, 0 if grid[y][x] else 1)

def draw_tetromino(tetromino):
    for i, row in enumerate(tetromino.shape):
        for j, cell in enumerate(row):
            if cell:
                rect = pygame.Rect((tetromino.x + j) * CELL_SIZE, (tetromino.y + i) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, tetromino.color, rect)

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    record_text = font.render(f"Highscore: {highscore}", True, WHITE)
    screen.blit(record_text, (10, 40))

# Основной цикл
fall_time = 0
fall_speed = 0.5
tetromino = Tetromino()
running = True
while running:
    dt = clock.tick(FPS) / 1000
    fall_time += dt

    for event in pygame.event.get():
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
                old_shape = tetromino.shape.copy()
                tetromino.rotate()
                if not tetromino.valid():
                    tetromino.shape = old_shape

    if fall_time > fall_speed:
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

    screen.fill(BLACK)  # Очистка экрана
    screen.blit(background, (0, 0))  # Отображение фона
    draw_grid()
    draw_tetromino(tetromino)
    draw_score()
    pygame.display.flip()

pygame.quit()

