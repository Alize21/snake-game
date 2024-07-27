import pygame

class Snake:


    def __init__(self,x_position,y_position):
        self.x = x_position
        self.y = y_position

    def draw_snake(self,screen):
        
        snake = pygame.draw.rect(screen,"green",(self.x,self.y,20,20))
        return snake

    def snake_mov(self):
        self.y-=0.1


class Apple:

    pass