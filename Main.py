import pygame
import random
from snake import *


pygame.init()

# Creating window
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
font = pygame.font.Font("project yang kubuat/snake-game/assets/font/game_over.ttf",200)

# Snake and apple initialization
snake = Snake(width//2,height//2)
apple = Apple(width,height)

clock = pygame.time.Clock()

def game_over():
    overtext = font.render("Game Over",True,"#02aa07")
    screen.blit(overtext,(width//2-190,height//2-70))

# Mainloop
game_over_flag = False
running = True
while running:


    if not game_over_flag:
        screen.fill("#5C9CB8")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Game keys        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            snake.set_direction("up")
        if keys[pygame.K_s]:
            snake.set_direction("down")
        if keys[pygame.K_d]:
            snake.set_direction("right")
        if keys[pygame.K_a]:
            snake.set_direction("left")


        # Detect colliding with snake and grow the snake body everytime the snake eats       
        if snake.x < apple.x+12 and snake.x+23 > apple.x and snake.y < apple.y+12 and snake.y+23 > apple.y:
            apple.x = random.randint(10,width-15)
            apple.y = random.randint(10,height-15)
            snake.grow()

        # Add new segment to the list
        snake.body.insert(0,[snake.x,snake.y])

        # Prevent the snake to grow more than it's length
        if len(snake.body) > snake.length:
            del snake.body[-1]
        
        # Game over
        if snake.check_collision():
            game_over_flag = True


        apple.draw_apple(screen)               
        snake.draw_snake(screen,snake.body)
        snake.update_position()


    else:

        game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.type == pygame.K_RETURN:
                running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
