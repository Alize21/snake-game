import pygame
from snake import *
import random

pygame.init()

# Creating window
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

# Snake and apple init
snake = Snake(width//2,height//2)
apple = Apple(width,height)

# Mainloop
running = True
while running:

    screen.fill("#5C9CB8")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        snake.set_direction("up")
    if keys[pygame.K_s]:
        snake.set_direction("down")
    if keys[pygame.K_d]:
        snake.set_direction("right")
    if keys[pygame.K_a]:
        snake.set_direction("left")

    snake.head.append(snake.x)
    snake.head.append(snake.y)

    # Detect colliding with snake        
    if snake.body[0][0] < apple.x+12 and snake.body[0][0]+23 > apple.x and snake.body[0][1] < apple.y+12 and snake.body[0][1]+23 > apple.y:
        apple.x = random.randint(10,width-15)
        apple.y = random.randint(10,height-15)
        #snake.length += 1
        snake.body.insert(0,snake.head[-2:])
        
   

    apple.draw_apple(screen)
            
    snake.draw_snake(screen,snake.body)

    snake.update_position(snake.body)

    pygame.display.update()



    print(snake.body)
pygame.quit()
