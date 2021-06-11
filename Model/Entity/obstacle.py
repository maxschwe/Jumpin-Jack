from Model.Entity.entity import Entity
import pygame

class Obstacle(Entity):
    def __init__(self, hitbox_coords):
        Entity.__init__(self, hitbox_coords)
        background_unscaled = pygame.image.load("Images/hintergrund2.png")
