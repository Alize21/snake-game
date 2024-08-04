import pygame
import random
from snake import *
from button import *


pygame.init()

# Creating window
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Game initialization
game_over_font = pygame.font.Font("assets/font/game_over.ttf",200)
score_font = pygame.font.Font("assets/font/game_over.ttf",70)
restart_img = pygame.image.load("assets/button/restart.png").convert_alpha()
exit_img = pygame.image.load("assets/button/exit.png").convert_alpha()
snake = Snake(width//2,height//2)
apple = Fruit(width,height)
restart_button = Button(510//2,580//2,restart_img,0.3)
exit_button = Button(830//2,580//2,exit_img,0.3)

def game_over():
    overtext = game_over_font.render("Game Over",True,"#02aa07")
    screen.blit(overtext,(width//2-190,height//2-70))

score_val = 0
def score():
    score = score_font.render("Score " + str(score_val),True,"black")
    screen.blit(score,(10,10))

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
            score_val += 10

        # Add new segment to the list
        snake.body.insert(0,[snake.x,snake.y])

        # Prevent the snake to grow more than it's length
        if len(snake.body) > snake.length:
            del snake.body[-1]
        
        # Game over
        if snake.check_collision():
            game_over_flag = True
        if snake.body[0][0] > width-23 or snake.body[0][0] < 1 or snake.body[0][1] > height-23 or snake.body[0][1] < 1:
            game_over_flag = True

        apple.draw_fruit(screen)               
        snake.draw_snake(screen,snake.body)
        score()
        
        snake.update_position()
        
        
    else:

        game_over()
        score()

        if exit_button.click():
            running = False
        if restart_button.click():
            snake.length = 1
            snake.x = width//2
            snake.y = height//2
            snake.direction = None
            del snake.body[1:]
            game_over_flag = False
            apple.x = random.randint(10,width-15)
            apple.y = random.randint(10,height-15)
            score_val = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        restart_button.draw(screen)
        exit_button.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
