import pygame

pygame.init()

win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("First game")
bg_image = pygame.image.load("Background.png")
bg = pygame.transform.scale(bg_image,(1000,500))

width = 1000
i=0
run = True
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(bg,(i,0))
    win.blit(bg,(i+width,0))
    if  i == -width:
        win.blit(bg,(width+i,0))
        i=0
    i-=1

    pygame.display.update()