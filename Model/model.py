import pygame
from Model.player import Player

class Model:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.observers = []
        background_unscaled = pygame.image.load("Images/hintergrund.png")
        self.background = pygame.transform.scale(background_unscaled, (self.width, self.height))
        self.background_x = 0
        self.speed = speed
        self.jumping = False
        self.player = Player(300, 600, 120, 120) 
        
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
        self.background_x += self.speed
        if self.background_x > self.width:
            self.background_x -= self.width
        self.player.left()
        self.update_observers()
    
    def right_key(self):
        self.background_x -= self.speed
        if self.background_x < -self.width:
            self.background_x += self.width
        self.player.right()
        self.update_observers()
    
    def up_key(self):
        pass
    
    def down_key(self):
        pass
    
    def space_key(self):
        self.player.space()

    def update(self):
        self.player.update()
        self.update_observers()

                