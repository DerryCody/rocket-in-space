import pygame

WIDTH=600
HEIGHT=600
TITLE="ROCKET IN SPACE"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg1=pygame.image.load("space bg.png")
i1=pygame.image.load("rocket.png")
x=300
y=300
go=False
while go==False:
    screen.blit(bg1,(0,0))
    screen.blit(i1,(x,y))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                y=y-10
            if event.key==pygame.K_s:
                y=y+10
            if event.key==pygame.K_a:
                x=x-10
            if event.key==pygame.K_d:
                x=x+10
        if event.type==pygame.QUIT:
          go=True
        if x==0 or x==500:
            go=True
        if y==0 or y==450:
            go=True
    pygame.display.update()