import pygame
from snake import *

pygame.init()

# Creating window
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

# Snake
snake = Snake(width//2,height//2)

# Mainloop
running = True
while running:

    screen.fill("#5C9CB8")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Snake.draw_snake(snake,screen)
    Snake.snake_mov(snake)

    pygame.display.update()

pygame.quit()
