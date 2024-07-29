import pygame

class Snake:


    def __init__(self,x_position,y_position):
        self.x = x_position
        self.y = y_position
        self.direction = "up"
        self.speed = 0.070

    def draw_snake(self,screen):
        
        snake = pygame.draw.rect(screen,"green",(self.x,self.y,20,20))
        return snake

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

       
class Apple:

    pass