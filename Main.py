import pygame
import random
from snake import *


pygame.init()

# Creating window
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

# Snake and apple init
snake = Snake(width//2,height//2)
apple = Apple(width,height)

clock = pygame.time.Clock()

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


    # Detect colliding with snake        
    if snake.x < apple.x+12 and snake.x+23 > apple.x and snake.y < apple.y+12 and snake.y+23 > apple.y:
        apple.x = random.randint(10,width-15)
        apple.y = random.randint(10,height-15)
        snake.length += 1

    snake.body.insert(0,[snake.x,snake.y])


    apple.draw_apple(screen)
            
    snake.draw_snake(screen,snake.body)

    snake.update_position()

    if len(snake.body) > snake.length:
        del snake.body[-1]

    pygame.display.update()


    clock.tick(30)
    
pygame.quit()
