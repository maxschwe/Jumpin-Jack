from Model.Entity.obstacle import Obstacle

class Chunk:
    def __init__(self, index, difficulty=0, object_list=[]):
        self.index = index
        self.difficulty = difficulty
        self.object_list = object_list
        for i in range(len(self.object_list)):
            self.object_list[i].move(self.index*1000, 0)

    def get_obstacles(self):
        return self.object_list[:]

    def generate_objects(self, difficulty=0): # random
        pass
    