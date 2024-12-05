import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")

# for the character circle
circle_x_position = 255
circle_y_position = 255
circle_radius = 15
vel_x = 10
vel_y = 10

jump =False

run = True
while run:
    win.fill((0,0,0))

    pygame.draw.circle(win,(255,255,255),(int(circle_x_position),int(circle_y_position)),circle_radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and circle_x_position >0:
        circle_x_position -= vel_x
    if userInput[pygame.K_RIGHT] and circle_x_position <500:
        circle_x_position +=vel_x

    if jump is False and  userInput[pygame.K_SPACE]:
        jump = True
    
    if jump is True:
        circle_y_position-=vel_y*3
        vel_y -=1
        if vel_y <-10:
            jump = False
            vel_y = 10
    
    pygame.time.delay(50)

    pygame.display.update()