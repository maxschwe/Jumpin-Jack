import pygame
from Model.Entity.player import Player
from Model.Entity.obstacle import Obstacle

class Model:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.observers = []
        background_unscaled = pygame.image.load("Images/hintergrund2.png")
        self.background = pygame.transform.scale(background_unscaled, (self.width, self.height))
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.jumping = False
        self.player = Player((0, 0, 120, 120), (35, 29, 50, 93), jump_force=20, gravity=1)
        self.obstacle = Obstacle((300, -100, 200, 50))
        self.alive = True
        
    def add_observer(self, observer): 
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
        
    def update_observers(self):
        for observer in self.observers:
            observer.update()
            
    def get_dimension(self):
        return (self.width, self.height)
    
    def left_key(self):
        self.dx -= self.speed
        self.player.left()
        self.update_observers()
        self.alive = True
        return self.alive
    
    def right_key(self):
        self.dx += self.speed
        self.player.right()
        self.update_observers()
        self.alive = True
        return self.alive
            
    def up_key(self):
        pass
    
    def down_key(self):
        pass
    
    def space_key(self):
        self.player.space()

    def update(self):
        self.dx = self.player.update(self.x, self.y, self.dx, [self.obstacle])
        self.x += self.dx
        self.y += self.dy
        if self.alive:
            self.update_observers()
        self.dx = 0
        self.dy = 0

    def restart(self):
        self.alive = True
        self.x = 0

                