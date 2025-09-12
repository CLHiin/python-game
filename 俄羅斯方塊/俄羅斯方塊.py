import pygame
import random
from pygame.locals import *
colors = [
    (0,0,0),
    (0,255,255),
    (25,25,112),
    (255,140,0),
    (139,0,139),
    (255,215,0),
    (220,20,60),
    (0,255,127),
]
class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
        [[1,2,6,7],[2,5,6,9]],
        [[2,3,5,6],[1,5,6,10]],
    ]
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = self.type +1
        self.rotation = 0
    
    def image2(self):
        return self.figures[self.type][0]

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

class Tetris:
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 100
    zoom = 20
    figure =Figure(3, 0)
    figure2=Figure(0, 0)
    spare  =Figure(0, 0)
    spare2 =Figure(0, 0)

    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = self.figure2
        self.figure2.x+=3
        self.figure2 =Figure(0, 0)
    
    def replace(self):
        self.spare2 =self.figure
        self.figure =self.spare
        self.figure.x+=3
        self.spare  =self.spare2
        self.spare.x=0
        self.spare.y=0

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or j + self.figure.x > self.width - 1 or j + self.figure.x < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1,-1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        if lines>=1:
            self.score += lines *100 +(lines-1)*50

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

# 初始化遊戲引擎
pygame.init()

# 定義一些顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("俄羅斯方塊")

# 迴圈，直到使用者點選關閉按鈕
done = False
clock = pygame.time.Clock()
fps = 25 
game = Tetris(20, 10)
counter = 0
pressing_down = False
c=6
ff=Figure(0,0)
while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0
    if game.score>=2000:    #分數>2000 速度0.2秒一格
        c=3
    elif game.score>=1000:  #分數>1000 速度0.24秒一格
        c=4
    elif game.score>=500:   #分數>500  速度0.28秒一格
        c=5

    if counter % (c+2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key==K_w:
                game.rotate()
            if event.key == pygame.K_DOWN or event.key==K_s:
                pressing_down = True
            if event.key == pygame.K_LEFT or event.key==K_a:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT or event.key==K_d:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key ==pygame.K_x:
                game.replace()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key==K_s:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):        #畫出20x10的格子
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:    #畫出已經掉落的方塊
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

            #畫出移動的方塊
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in game.figure.image():
                pygame.draw.rect(screen, colors[game.figure.color],
                                 [game.x + game.zoom * (j + game.figure.x) + 1,
                                  game.y + game.zoom * (i + game.figure.y) + 1,
                                  game.zoom - 2, game.zoom - 2])
    
    for i in range(4):                  #下次的方塊
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [320 + 20*i , 100 + 20* j, 20 , 20], 1)
            pygame.draw.rect(screen, GRAY, [0 + 20*i , 100 + 20* j, 20 , 20], 1)
            if i * 4 + j in game.figure2.image():
                pygame.draw.rect(screen, colors[game.figure2.color],
                                 [320 + 20 * j +1 , 100 + 20 * i +1, 18, 19])
            if i * 4 + j in game.spare.image():
                pygame.draw.rect(screen, colors[game.spare.color],
                                 [0 + 20 * j +1 , 100 + 20 * i +1, 18, 19])
            
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over ", True, (255, 0, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [10, 200])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()