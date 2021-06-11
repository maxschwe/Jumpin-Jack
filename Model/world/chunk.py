from Model.Entity.obstacle import Obstacle
import random

DISTANCE_MIN = 50
DISTANCE_MAX = 200
WIDTH_MIN = 50
WIDTH_MAX = 300
HEIGHT_MIN = 50
HEIGHT_MAX = 100

class Chunk:
    def __init__(self, index, difficulty=0, object_list=[]):
        self.index = index
        self.difficulty = difficulty
        self.generate_objects()
        for i in range(len(self.object_list)):
            self.object_list[i].move(self.index*1000, 0)
        self.distances = [] #0: 0 bis 1

    def get_obstacles(self):
        return self.object_list[:]

    def generate_objects(self, difficulty=2):
        self.object_list = []
        space_available = True
        vorgänger = [0, 0, 0, 0]
        current = [0, 0, 0, 0]
        while space_available:
            random_x = vorgänger[0] + vorgänger[2] + random.randint(DISTANCE_MIN, DISTANCE_MAX)
            random_width = random.randint(WIDTH_MIN, WIDTH_MAX)
            random_height = random.randint(HEIGHT_MIN, HEIGHT_MAX)

            y_min = vorgänger[1] - 45 * difficulty
            
            # vorgänger ist maximal 100 entfernt vom nächsten
            if y_min < - 600 + random_height + 100: # aktueller darf nicht über das fenster kommen
                y_min = - 600 + random_height + 100
            
            y_max = vorgänger[1] + 50 * difficulty
            if y_max > 0:
                y_max = 0
            y_pred = random.randint(y_min, y_max)
            # print(y_pred)
            
            random_y = y_pred

            if random_x + random_width > 1000:
                space_available = False
            else:
                current = [random_x, random_y, random_width, random_height]
                self.object_list.append(Obstacle(current))
                vorgänger = current[:]

            if current[1] > vorgänger[1] + 100:
                print("gotcha")
                print(current[1], vorgänger[1])
            