from Model.Entity.obstacle import Obstacle

class Chunk:
    def __init__(self, index, difficulty=0, object_list=[]):
        self.index = index
        self.difficulty = difficulty
        self.object_list = object_list

    def get_obstacles(self):
        return self.object_list

    def generate_objects(self, difficulty=0): # random
        pass

    