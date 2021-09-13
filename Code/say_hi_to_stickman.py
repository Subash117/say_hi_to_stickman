import pygame,sys
from pygame.locals import *

pygame.init()

fps=40
fpsclock=pygame.time.Clock()

DISPLAY=pygame.display.set_mode((500,500))
pygame.display.set_caption('Say HI!!')

BLACK=(0,0,0)
BLUE=(0,0,128)

hand_move_y=250
wid=2
direction='up'

while True:
    DISPLAY.fill(BLACK)
    if direction=='up':
        hand_move_y-=5
        pygame.draw.circle(DISPLAY,BLUE,(250,100),50,wid)
        pygame.draw.line(DISPLAY,BLUE,(250,150),(250,300),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,300),(180,400),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,300),(320,400),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,200),(330,250),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,200),(170,hand_move_y),wid)
        if hand_move_y==150:
            direction='down'
    elif direction=='down':
        hand_move_y+=5
        pygame.draw.circle(DISPLAY,BLUE,(250,100),50,wid)
        pygame.draw.line(DISPLAY,BLUE,(250,150),(250,300),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,300),(180,400),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,300),(320,400),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,200),(330,250),wid)
        pygame.draw.line(DISPLAY,BLUE,(250,200),(170,hand_move_y),wid)
        if hand_move_y==250:
            direction='up'

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsclock.tick(fps)