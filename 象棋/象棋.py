import pygame
import random
from pygame.locals import *

red = (255,0,0)
green=(0,255,0)
blue =(0,0,255)
GRAY  =(128, 128, 128)
WHITE =(255,255,255)
BLACK =(0,0,0)
BB_L=False
RR_L=False
pygame.init()#視窗
surface = pygame.display.set_mode((600,700))
pygame.display.set_caption("象棋(測試版)")
font = pygame.font.SysFont('Calibri', 50, True, False)
step_font2 =font.render(("Black win!!!" ), True, BLACK)
step_font3 =font.render(("Red win!!!" ), True, red)
soldier1  =pygame.image.load("兵.jpg")
soldier2  =pygame.image.load("炮.jpg")
soldier3  =pygame.image.load("俥.jpg")
soldier4  =pygame.image.load("傌.jpg")
soldier5  =pygame.image.load("相.jpg")
soldier6  =pygame.image.load("仕.jpg")
soldier10 =pygame.image.load("帥.jpg")
soldier_1 =pygame.image.load("卒.jpg")
soldier_2 =pygame.image.load("包.jpg")
soldier_3 =pygame.image.load("車.jpg")
soldier_4 =pygame.image.load("馬.jpg")
soldier_5 =pygame.image.load("象.jpg")
soldier_6 =pygame.image.load("士.jpg")
soldier_10=pygame.image.load("將.jpg")

class Chinese_chess:
    determination = 0
    height= 0
    width = 0
    switch= 0
    field = [
        [-3 ,-4 ,-5 ,-6 ,-10 ,-6 ,-5 ,-4 ,-3 ],
        [ 0 , 0 , 0 , 0 ,  0 , 0 , 0 , 0 , 0 ],
        [ 0 ,-2 , 0 , 0 ,  0 , 0 , 0 ,-2 , 0 ],
        [-1 , 0 ,-1 , 0 ,- 1 , 0 ,-1 , 0 ,-1 ],
        [ 0 , 0 , 0 , 0 ,  0 , 0 , 0 , 0 , 0 ],

        [ 0 , 0 , 0 , 0 ,  0 , 0 , 0 , 0 , 0 ],
        [ 1 , 0 , 1 , 0 ,  1 , 0 , 1 , 0 , 1 ],
        [ 0 , 2 , 0 , 0 ,  0 , 0 , 0 , 2 , 0 ],
        [ 0 , 0 , 0 , 0 ,  0 , 0 , 0 , 0 , 0 ],
        [ 3 , 4 , 5 , 6 , 10 , 6 , 5 , 4 , 3 ],
    ]
    zoom = 30
    keep_x = 0
    keep_y = 0
    step = 0
    x = 50+zoom/2
    y = 50+zoom/2
    sx= 0
    sy= 0

    def Right (self):
        self.sx += 1
        if self.sx>8:
            self.sx=0
    def Left (self):
        self.sx -= 1
        if self.sx<0:
            self.sx=8
    def Down (self):
        self.sy += 1
        if self.sy>9:
            self.sy=0
    def Up (self):
        self.sy -= 1
        if self.sy<0:
            self.sy=9

    def change (self):
        if self.field[self.sy][self.sx]==7 or self.field[self.sy][self.sx]>89: #代表可以移動
            self.field[self.sy][self.sx] = self.field[self.keep_y][self.keep_x]
            self.field[self.keep_y][self.keep_x] = 0
            self.switch=(self.switch+1)%2
            self.rect()
        else :
            self.rect()
            if self.switch == 0 :
                self.mobileR()
            else :
                self.mobileB()

    def rect (self):
        self.determination = 0
        self.keep_x = self.sx
        self.keep_y = self.sy
        for i in range(9):
                for j in range(10):
                    if self.field[j][i] > 89 :
                        self.field[j][i]-=100
        for i in range(3,6):
            for j in range(0,3):
                if self.field[j][i] == -10:
                    for a in range(j+1,10):
                        if self.field[a][i] == 0 or self.field[a][i]==10:
                            if self.field[a][i]==10:
                                if self.switch == 1:
                                    self.field[a][i]+=100
                                else :
                                    self.field[j][i]+=100
                        else :
                            break

    def mobileR (self):
        if   self.field[self.sy][self.sx] == 1 :#兵
            if self.sy >=5:
                if self.field[self.sy-1][self.sx]<=0:
                    self.field[self.sy-1][self.sx]+=100
            else :
                if self.field[self.sy-1][self.sx] <=0:
                    self.field[self.sy-1][self.sx]+=100
                if self.sx-1 >=0 and self.field[self.sy][self.sx-1] <=0 :
                    self.field[self.sy][self.sx-1] +=100
                if self.sx+1 < 9 and self.field[self.sy][self.sx+1] <=0 :
                    self.field[self.sy][self.sx+1]+=100
        elif self.field[self.sy][self.sx] == 2 :#炮
            if self.sx!=0:
                for i in range (self.sx-1,-1,-1):
                    if  self.field[self.sy][i] == 0 and self.determination == 0 :
                        self.field[self.sy][i] +=100
                    elif self.field[self.sy][i] < 0 and self.determination == 1 :
                        self.field[self.sy][i] +=100
                        break
                    elif self.field[self.sy][i]!= 0 :
                        self.determination+=1
            if self.sx!=8:
                self.determination = 0
                for i in range (self.sx+1,9):
                    if   self.field[self.sy][i] == 0 and self.determination == 0 :
                        self.field[self.sy][i]+=100
                    elif self.field[self.sy][i] < 0  and self.determination == 1 :
                        self.field[self.sy][i]+=100
                        break
                    elif self.field[self.sy][i]!=0 :
                        self.determination+=1
            if self.sy!=0:
                self.determination = 0
                for i in range (self.sy-1,-1,-1):
                    if   self.field[i][self.sx]== 0 and self.determination == 0 :
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx] < 0 and self.determination == 1 :
                        self.field[i][self.sx]+=100
                        break
                    elif self.field[i][self.sx]!= 0 :
                        self.determination+=1
            if self.sy!=9:
                self.determination = 0
                for i in range (self.sy+1,10):
                    if   self.field[i][self.sx]== 0 and self.determination == 0:
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx] < 0 and self.determination == 1 :
                        self.field[i][self.sx]+=100
                        break
                    elif self.field[i][self.sx]!= 0 :
                        self.determination+=1
        elif self.field[self.sy][self.sx] == 3 :#俥
            if self.sx!=0:
                for i in range (self.sx-1,-1,-1):
                    if  self.field[self.sy][i]== 0 :
                        self.field[self.sy][i]+=100
                    elif self.field[self.sy][i]< 0 :
                        self.field[self.sy][i]+=100
                        break
                    else :
                        break
            if self.sx!=8:
                for i in range (self.sx+1,9):
                    if  self.field[self.sy][i]== 0:
                        self.field[self.sy][i]+=100
                    elif self.field[self.sy][i]<0 :
                        self.field[self.sy][i]+=100
                        break
                    else :
                        break
            if self.sy!=0:
                for i in range (self.sy-1,-1,-1):
                    if  self.field[i][self.sx]== 0:
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx]< 0 :
                        self.field[i][self.sx]+=100
                        break
                    else :
                        break
            if self.sy!=9:
                for i in range (self.sy+1,10):
                    if  self.field[i][self.sx]== 0:
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx]< 0 :
                        self.field[i][self.sx]+=100
                        break
                    else :
                        break  
        elif self.field[self.sy][self.sx] == 4 :#傌
            if self.sy>1 :
                if self.field[self.sy-1][self.sx] == 0 :
                    if self.field[self.sy-2][self.sx-1] <= 0:
                        self.field[self.sy-2][self.sx-1]+=100
                    if self.field[self.sy-2][self.sx+1] <= 0:
                        self.field[self.sy-2][self.sx+1]+=100
            if self.sy<8 :
                if self.field[self.sy+1][self.sx] == 0 :
                    if self.field[self.sy+2][self.sx-1] <= 0:
                        self.field[self.sy+2][self.sx-1]+=100
                    if self.field[self.sy+2][self.sx+1] <= 0:
                        self.field[self.sy+2][self.sx+1]+=100
            if self.sx>1 :
                if self.field[self.sy][self.sx-1] == 0 :
                    if self.field[self.sy+1][self.sx-2] <= 0:
                        self.field[self.sy+1][self.sx-2]+=100
                    if self.field[self.sy-1][self.sx-2] <= 0:
                        self.field[self.sy-1][self.sx-2]+=100
            if self.sx<7 :
                if self.field[self.sy][self.sx+1] == 0 :
                    if self.field[self.sy+1][self.sx+2] <= 0:
                        self.field[self.sy+1][self.sx+2]+=100
                    if self.field[self.sy-1][self.sx+2] <= 0:
                        self.field[self.sy-1][self.sx+2]+=100
        elif self.field[self.sy][self.sx] == 5 :#相
            if self.sy!=9 :
                if self.sx!=8:
                    if  self.field[self.sy+1][self.sx+1] == 0 and self.field[self.sy+2][self.sx+2] <= 0:
                        self.field[self.sy+2][self.sx+2]+=100
                if self.sx!=0:
                    if  self.field[self.sy+1][self.sx-1] == 0 and self.field[self.sy+2][self.sx-2] <= 0:
                        self.field[self.sy+2][self.sx-2]+=100
            if self.sy!=5 :
                if self.sx!=8:
                    if  self.field[self.sy-1][self.sx-1] == 0 and self.field[self.sy-2][self.sx-2] <= 0:
                        self.field[self.sy-2][self.sx-2]+=100
                if self.sx!=0:
                    if  self.field[self.sy-1][self.sx+1] == 0 and self.field[self.sy-2][self.sx+2] <= 0:
                        self.field[self.sy-2][self.sx+2]+=100
        elif self.field[self.sy][self.sx] == 6 :#仕
            if self.sx!=3 :
                if self.sy!=9:
                    if self.field[self.sy+1][self.sx-1] <= 0:
                        self.field[self.sy+1][self.sx-1]+=100
                if self.sy!=7:
                    if self.field[self.sy-1][self.sx-1] <= 0:
                        self.field[self.sy-1][self.sx-1]+=100
            if self.sx!=5 :
                if self.sy!=9:
                    if self.field[self.sy+1][self.sx+1] <= 0:
                        self.field[self.sy+1][self.sx+1]+=100
                if self.sy!=7:
                    if self.field[self.sy-1][self.sx+1] >= 0:
                        self.field[self.sy-1][self.sx+1]+=100
        elif self.field[self.sy][self.sx] == 10:#帥
            if self.sy!= 9:
                if  self.field[self.sy+1][self.sx] <= 0:
                    self.field[self.sy+1][self.sx] +=100
            if self.sy!= 7:
                if  self.field[self.sy-1][self.sx] <= 0:
                    self.field[self.sy-1][self.sx] +=100
            if self.sx!=3:
                if  self.field[self.sy][self.sx-1] <= 0:
                    self.field[self.sy][self.sx-1] +=100
            if self.sx!=5:
                if  self.field[self.sy][self.sx+1] <= 0:
                    self.field[self.sy][self.sx+1] +=100

    def mobileB (self):
        if   self.field[self.sy][self.sx] == -1 :#卒
            if self.sy <5:
                if  self.field[self.sy+1][self.sx]>= 0:
                    self.field[self.sy+1][self.sx]+=100
            else :
                if  self.field[self.sy+1][self.sx]>= 0:
                    self.field[self.sy+1][self.sx]+=100
                if  self.sx-1 >=0 and self.field[self.sy][self.sx-1]>= 0:
                    self.field[self.sy][self.sx-1]+=100
                if  self.sx+1 < 9 and self.field[self.sy][self.sx+1]>= 0:
                    self.field[self.sy][self.sx+1]+=100
        elif self.field[self.sy][self.sx] == -2 :#炮
            if self.sx!=0:
                for i in range (self.sx-1,-1,-1):
                    if  self.field[self.sy][i] == 0 and self.determination == 0 :
                        self.field[self.sy][i] +=100
                    elif self.field[self.sy][i] > 0 and self.determination == 1 :
                        self.field[self.sy][i] +=100
                        break
                    elif self.field[self.sy][i]!= 0 :
                        self.determination+=1
            if self.sx!=8:
                self.determination = 0
                for i in range (self.sx+1,9):
                    if   self.field[self.sy][i] == 0 and self.determination == 0 :
                        self.field[self.sy][i]+=100
                    elif self.field[self.sy][i] > 0  and self.determination == 1 :
                        self.field[self.sy][i]+=100
                        break
                    elif self.field[self.sy][i]!=0 :
                        self.determination+=1
            if self.sy!=0:
                self.determination = 0
                for i in range (self.sy-1,-1,-1):
                    if   self.field[i][self.sx]== 0 and self.determination == 0 :
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx] > 0 and self.determination == 1 :
                        self.field[i][self.sx]+=100
                        break
                    elif self.field[i][self.sx]!= 0 :
                        self.determination+=1
            if self.sy!=9:
                self.determination = 0
                for i in range (self.sy+1,10):
                    if   self.field[i][self.sx]== 0 and self.determination == 0:
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx] > 0 and self.determination == 1 :
                        self.field[i][self.sx]+=100
                        break
                    elif self.field[i][self.sx]!= 0 :
                        self.determination+=1
        elif self.field[self.sy][self.sx] == -3 :#車
            if self.sx!=0:
                for i in range (self.sx-1,-1,-1):
                    if  self.field[self.sy][i]== 0 :
                        self.field[self.sy][i]+=100
                    elif self.field[self.sy][i]> 0 :
                        self.field[self.sy][i]+=100
                        break
                    else :
                        break
            if self.sx!=8:
                for i in range (self.sx+1,9):
                    if  self.field[self.sy][i]== 0:
                        self.field[self.sy][i]+=100
                    elif self.field[self.sy][i]>0 :
                        self.field[self.sy][i]+=100
                        break
                    else :
                        break
            if self.sy!=0:
                for i in range (self.sy-1,-1,-1):
                    if  self.field[i][self.sx]== 0:
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx]> 0 :
                        self.field[i][self.sx]+=100
                        break
                    else :
                        break
            if self.sy!=9:
                for i in range (self.sy+1,10):
                    if  self.field[i][self.sx]== 0:
                        self.field[i][self.sx]+=100
                    elif self.field[i][self.sx]> 0 :
                        self.field[i][self.sx]+=100
                        break
                    else :
                        break
        elif self.field[self.sy][self.sx] == -4 :#馬
            if self.sy>1 :
                if self.field[self.sy-1][self.sx] == 0 :
                    if  self.field[self.sy-2][self.sx-1]>= 0:
                        self.field[self.sy-2][self.sx-1]+=100
                    if  self.field[self.sy-2][self.sx+1]>= 0:
                        self.field[self.sy-2][self.sx+1]+=100
            if self.sy<8 :
                if self.field[self.sy+1][self.sx] == 0 :
                    if  self.field[self.sy+2][self.sx-1]>= 0:
                        self.field[self.sy+2][self.sx-1]+=100
                    if  self.field[self.sy+2][self.sx+1]>= 0:
                        self.field[self.sy+2][self.sx+1]+=100
            if self.sx>1 :
                if self.field[self.sy][self.sx-1] == 0 :
                    if  self.field[self.sy+1][self.sx-2]>= 0:
                        self.field[self.sy+1][self.sx-2]+=100
                    if  self.field[self.sy-1][self.sx-2]>= 0:
                        self.field[self.sy-1][self.sx-2]+=100
            if self.sx<7 :
                if self.field[self.sy][self.sx+1] == 0 :
                    if  self.field[self.sy+1][self.sx+2]>= 0:
                        self.field[self.sy+1][self.sx+2]+=100
                    if  self.field[self.sy-1][self.sx+2]>= 0:
                        self.field[self.sy-1][self.sx+2]+=100
        elif self.field[self.sy][self.sx] == -5 :#象
            if self.sy!=4 :
                if self.sx!=8:
                    if  self.field[self.sy+1][self.sx+1] == 0 and self.field[self.sy+2][self.sx+2] >= 0:
                        self.field[self.sy+2][self.sx+2]+=100
                if  self.sx!=0:
                    if  self.field[self.sy+1][self.sx-1] == 0 and self.field[self.sy+2][self.sx-2] >= 0:
                        self.field[self.sy+2][self.sx-2]+=100
            if self.sy!=0 :
                if self.sx!=8:
                    if  self.field[self.sy-1][self.sx-1] == 0 and self.field[self.sy-2][self.sx-2] >= 0:
                        self.field[self.sy-2][self.sx-2]+=100
                if self.sx!=0:
                    if  self.field[self.sy-1][self.sx+1] == 0 and self.field[self.sy-2][self.sx+2] >= 0:
                        self.field[self.sy-2][self.sx+2]+=100
        elif self.field[self.sy][self.sx] == -6 :#士
            if self.sx!=3 :
                if self.sy!=2:
                    if  self.field[self.sy+1][self.sx-1]>= 0:
                        self.field[self.sy+1][self.sx-1]+=100
                if self.sy!=0:
                    if  self.field[self.sy-1][self.sx-1]>= 0:
                        self.field[self.sy-1][self.sx-1]+=100
            if self.sx!=5 :
                if self.sy!=2:
                    if  self.field[self.sy+1][self.sx+1]>= 0:
                        self.field[self.sy+1][self.sx+1]+=100
                if self.sy!=0:
                    if  self.field[self.sy-1][self.sx+1]>= 0:
                        self.field[self.sy-1][self.sx+1]+=100
        elif self.field[self.sy][self.sx] == -10:#將
            if self.sy!= 2:
                if  self.field[self.sy+1][self.sx]>= 0:
                    self.field[self.sy+1][self.sx]+=100
            if self.sy!= 0:
                if  self.field[self.sy-1][self.sx]>= 0:
                    self.field[self.sy-1][self.sx]+=100
            if self.sx!=3:
                if  self.field[self.sy][self.sx-1]>= 0:
                    self.field[self.sy][self.sx-1]+=100
            if self.sx!=5:
                if  self.field[self.sy][self.sx+1]>= 0:
                    self.field[self.sy][self.sx+1]+=100

class Cube:
    fil=[1,2,3,4,5,6,10,-1,-2,-3,-4,-5,-6,-10]
    dic={
         1: soldier1 , 2: soldier2 , 3: soldier3 , 4: soldier4 , 5: soldier5 , 6: soldier6 , 10: soldier10 ,
        -1: soldier_1,-2: soldier_2,-3: soldier_3,-4: soldier_4,-5: soldier_5,-6: soldier_6,-10: soldier_10 
    }
    def picture(self,s,x,y):
        for i in range(0,14):
            if s == self.fil[i] or s-100 == self.fil[i] :
                surface.blit(self.dic[self.fil[i]],[x,y])

done = False
game = Chinese_chess()
game2= Cube()
clock= pygame.time.Clock()   #建立時間元件

while not done:  # 程式主迴圈
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
        if event.type == KEYDOWN:
            if(event.key==K_UP or event.key==K_w):
                game.Up()
            if(event.key==K_DOWN or event.key==K_s):
                game.Down()
            if(event.key==K_LEFT or event.key==K_a):
                game.Left()
            if(event.key==K_RIGHT or event.key==K_d):
                game.Right()
            if event.key == K_k:
                game.change()

    surface.fill(WHITE)
    B_l=0
    R_l=0

    for i in range(4):#紅色的
        for j in range(8):
            pygame.draw.rect(surface , BLACK , [game.x + game.zoom * 2 * j ,game.y + game.zoom * 2 * i , game.zoom * 2 , game.zoom * 2 ], 2 )
    pygame.draw.line(surface , BLACK , (game.x + game.zoom * 2 * 3 ,game.y + game.zoom * 2 * 7),(game.x + game.zoom * 2 * 5 ,game.y + game.zoom * 2 * 9), 4)
    pygame.draw.line(surface , BLACK , (game.x + game.zoom * 2 * 3 ,game.y + game.zoom * 2 * 9),(game.x + game.zoom * 2 * 5 ,game.y + game.zoom * 2 * 7), 4)
    pygame.draw.rect(surface , BLACK , [game.x , game.y + game.zoom * 8 , game.zoom * 16 , game.zoom * 2 ],2)#中間的空隙
    for i in range(4):#黑色的
        for j in range(8):
            pygame.draw.rect(surface , BLACK , [
                                                game.x + game.zoom * 2 * j ,
                                                game.y + game.zoom *10 + game.zoom * 2 * i ,
                                                game.zoom * 2 , game.zoom * 2 ],2)
    pygame.draw.line(surface , BLACK , (game.x + game.zoom * 2 * 3 ,game.y + game.zoom * 2 * 2),(game.x + game.zoom * 2 * 5 ,game.y + game.zoom * 2 * 0), 4)
    pygame.draw.line(surface , BLACK , (game.x + game.zoom * 2 * 3 ,game.y + game.zoom * 2 * 0),(game.x + game.zoom * 2 * 5 ,game.y + game.zoom * 2 * 2), 4)

    for i in range(9):
        for j in range(10):
            if  game.field[j][i] != 0:
                game2.picture( game.field[j][i] , game.x + game.zoom * (2 * i - 0.5) , game.y + game.zoom *( 2 * j - 0.5))
            if  game.sx==i and game.sy==j:
                pygame.draw.rect  (surface , blue , [game.x + game.zoom * (2 * i - 0.5) - 2 , game.y + game.zoom *(2 * j - 0.5) - 2 , game.zoom + 3 , game.zoom + 3 ], 2)
            if  game.field[j][i] > 10 :
                pygame.draw.circle(surface , green, (game.x + game.zoom * 2 * i , game.y + game.zoom *  2 * j ) , 10 )
            if  game.field[j][i]!=10:
                R_l+=1
            if  game.field[j][i]!=-10:
                B_l+=1

    if   B_l == 90 :
        surface.blit(step_font3,[200,310])
    elif R_l == 90 :
        surface.blit(step_font2,[200,310])

    clock.tick(25)
    pygame.display.flip()

pygame.quit()