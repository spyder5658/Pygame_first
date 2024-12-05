import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")

# for the character circle
circle_x_position = 255
circle_y_position = 255
circle_radius = 15
vel = 5

run = True
while run:
    win.fill((0,0,0))

    pygame.draw.circle(win,(255,255,255),(int(circle_x_position),int(circle_y_position)),circle_radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and circle_x_position >0:
        circle_x_position -= vel
    if userInput[pygame.K_RIGHT] and circle_x_position <500:
        circle_x_position +=vel
    if userInput[pygame.K_UP] and circle_y_position >0:
        circle_y_position -= vel
    if userInput[pygame.K_DOWN] and circle_y_position < 500:
        circle_y_position += vel
    pygame.time.delay(15)

    pygame.display.update()