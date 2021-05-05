from Model.entity import Entity

class Obstacle(Entity):
    def __init__(self, hitbox_coords):
        Entity.__init__(self, hitbox_coords)
