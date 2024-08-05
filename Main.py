import pygame
import random
from snake import *
from button import *


pygame.init()
# Game window
width,height = 800,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Load assets
game_over_font = pygame.font.Font("assets/font/game_over.ttf",200)
score_font = pygame.font.Font("assets/font/game_over.ttf",70)
play_img = pygame.image.load("assets/button/play.png").convert_alpha()
exit_from_menu_img = pygame.image.load("assets/button/exit from menu.png").convert_alpha()
restart_img = pygame.image.load("assets/button/restart.png").convert_alpha()
exit_img = pygame.image.load("assets/button/exit.png").convert_alpha()

# Game init
snake = Snake(width//2,height//2)
apple = Fruit(width,height)
play_button = Button(10,10,play_img,0.4)
exit_from_menu_button = Button(620,10,exit_from_menu_img,0.4)
restart_button = Button(510//2,580//2,restart_img,0.3)
exit_button = Button(830//2,580//2,exit_img,0.3)

def game_over():
    overtext = game_over_font.render("Game Over",True,"#02aa07")
    screen.blit(overtext,(width//2-190,height//2-70))

def score():
    score = score_font.render("Score " + str(score_val),True,"black")
    screen.blit(score,(10,10))

score_val = 0
state = "menu"
running = True

# Mainloop
while running:

    screen.blit(screen,(width,height))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    if state == "menu":

        screen.fill("green")

        if play_button.click():
            snake.length = 2
            snake.x = width//2
            snake.y = height//2
            snake.direction = None
            del snake.body[1:]
            apple.x = random.randint(10,width-15)
            apple.y = random.randint(10,height-15)
            score_val = 0
            state = "play"
        
        if exit_from_menu_button.click():
            running = False

        play_button.draw(screen)
        exit_from_menu_button.draw(screen)

    elif state == "play":
       
        screen.fill("#5C9CB8")                
            
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
        if len(snake.body) > snake.length:
            del snake.body[-1]
            
        # Game over
        if snake.check_collision():
            state = "game over"
        if snake.body[0][0] > width-23 or snake.body[0][0] < 1 or snake.body[0][1] > height-23 or snake.body[0][1] < 1:
            state = "game over"

        snake.update_position()
        apple.draw_fruit(screen)               
        snake.draw_snake(screen,snake.body)
        score()
            
        
    elif state == "game over":

        screen.fill("#5C9CB8")                

        if exit_button.click():
            state = "menu"

        if restart_button.click():
            snake.length = 1
            snake.x = width//2
            snake.y = height//2
            snake.direction = None
            del snake.body[1:]
            apple.x = random.randint(10,width-15)
            apple.y = random.randint(10,height-15)
            score_val = 0
            state = "play"

        apple.draw_fruit(screen)               
        snake.draw_snake(screen,snake.body)
        restart_button.draw(screen)
        exit_button.draw(screen)
        game_over()
        score()

    pygame.display.update()
    clock.tick(30)

pygame.quit()