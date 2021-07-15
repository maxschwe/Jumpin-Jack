from Model.Entity.obstacle import Obstacle
import random

class Chunk:
    def __init__(self, index, object_list=[]):
        self.index = index
        self.object_list = object_list
        for i in range(len(self.object_list)):
            self.object_list[i].move(self.index*1000, 0)

    def get_obstacles(self):
        return self.object_list[:]
    