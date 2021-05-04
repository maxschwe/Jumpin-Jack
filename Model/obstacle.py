from Model.entity import Entity

class Obstacle(Entity):
    def __init__(self, hitbox_coords, speed):
        Entity.__init__(self, hitbox_coords)
        self.speed = speed
        self.move(50,123)
        
    def left(self): # press left
        self.move(self.speed, 0)
        
    def right(self): # press right
        self.move(- self.speed, 0)