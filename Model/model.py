import pygame
from Model.player import Player
from Model.obstacle import Obstacle

class Model:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.observers = []
        background_unscaled = pygame.image.load("Images/hintergrund.png")
        self.background = pygame.transform.scale(background_unscaled, (self.width, self.height))
        self.x = 300
        self.speed = speed
        self.jumping = False
        self.player = Player((300, 480, 120, 120), (35, 25, 50, 95)) #1.Tupel: Coords, 2.Tupel: Hitbox-Coords
        self.obstacle = Obstacle((800, 500, 200, 100))
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
        self.x -= self.speed
        self.player.left()
        real_hitbox = self.obstacle.hitbox.move(-self.x, 0)
        collided = self.player.check_collision(real_hitbox)
        if collided:
            change = (real_hitbox.x + real_hitbox.width) - self.player.hitbox.x
            self.x += change
        self.update_observers()
        self.alive = not collided
        return self.alive
    
    def right_key(self):
        self.x += self.speed
        self.player.right() 
        real_hitbox = self.obstacle.hitbox.move(-self.x, 0)
        collided =  self.player.check_collision(real_hitbox)
        if collided:
            change = (self.player.hitbox.x + self.player.hitbox.width) - real_hitbox.x
            self.x -= change 
        self.update_observers()
        self.alive = not collided
        return self.alive
            
    def up_key(self):
        pass
    
    def down_key(self):
        pass
    
    def space_key(self):
        self.player.space()
        
    def check_collisions(self):
        collision = self.player.check_collision(self.obstacle)
        if collision:
            print('collided')

    def update(self):
        self.player.update()
        if self.alive:
            self.update_observers()

    def restart(self):
        self.alive = True
        self.x = 300

                