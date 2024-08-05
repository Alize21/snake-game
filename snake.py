import pygame
import random

class Snake:


    def __init__(self,x_position,y_position):
        self.x = x_position
        self.y = y_position
        self.direction = None
        self.speed = 10
        self.body = [[x_position,y_position]]
        self.length = 1

    def draw_snake(self,screen,snakebody):
        for x,y in snakebody:
            pygame.draw.rect(screen,"green",(x,y,20,20))
            

    def update_position(self):       
        if self.direction == "up":
            self.y-=self.speed
        if self.direction == "down":
            self.y+=self.speed
        if self.direction == "left":
            self.x-=self.speed
        if self.direction == "right":
            self.x+=self.speed
    
    def set_direction(self,new_direction):
        if self.direction == "up" and new_direction !="down":
            self.direction = new_direction
        elif self.direction == "down" and new_direction !="up":
            self.direction = new_direction
        elif self.direction == "right" and new_direction !="left":
            self.direction = new_direction
        elif self.direction == "left" and new_direction !="right":
            self.direction = new_direction
        elif self.direction == None:
            self.direction = new_direction

    def grow(self):
        self.length += 1.5
        
    def check_collision(self):
        for segment in self.body[2:]:
            if self.x == segment[0] and self.y == segment[1]:
                return True
        return False 
       
class Fruit:

    def __init__(self,width_screen,height_screen):
        self.x = random.randint(10,width_screen-15)
        self.y = random.randint(10,height_screen-15)

    def draw_fruit(self,screen):
        circle_pos = (self.x,self.y)
        pygame.draw.circle(screen,"red",circle_pos,7)
