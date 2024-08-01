import pygame
import random

class Snake:


    def __init__(self,x_position,y_position):
        self.x = x_position
        self.y = y_position
        self.direction = "up"
        self.speed = 0.5
        self.head = []
        self.body = [[100,250]]

    def draw_snake(self,screen,snake_body_pos):
        for x,y in snake_body_pos:
            pygame.draw.rect(screen,"green",(x,y,20,20))
            

    def update_position(self,snake_body):
        if self.direction == "up":
            snake_body[0][1]-=self.speed
        if self.direction == "down":
            snake_body[0][1]+=self.speed
        if self.direction == "left":
            snake_body[0][0]-=self.speed
        if self.direction == "right":
            snake_body[0][0]+=self.speed
    
    def set_direction(self,new_direction):
        if self.direction == "up" and new_direction !="down":
            self.direction = new_direction
        elif self.direction == "down" and new_direction !="up":
            self.direction = new_direction
        elif self.direction == "right" and new_direction !="left":
            self.direction = new_direction
        elif self.direction == "left" and new_direction !="right":
            self.direction = new_direction

       
class Apple:

    def __init__(self,width_screen,height_screen):
        self.x = random.randint(10,width_screen-15)
        self.y = random.randint(10,height_screen-15)


    def draw_apple(self,screen):
        circle_pos = (self.x,self.y)
        pygame.draw.circle(screen,"red",circle_pos,7)