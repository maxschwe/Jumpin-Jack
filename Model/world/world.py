from Model.world.chunk import Chunk
from Model.Entity.obstacle import Obstacle
from PIL import Image
import random
import os
import time

PATH_FLOATING_OBJECTS = "Images/objects/floating_objects"
PATH_GROUND_DEATH = "Images/objects/ground_death"
PATH_GROUND_OBJECTS = "Images/objects/ground_objects"

DISTANCE_MIN = 100
DISTANCE_MAX = 200
WIDTH_MIN = 50
WIDTH_MAX = 300
HEIGHT_MIN = 50
HEIGHT_MAX = 95


class World:
    def __init__(self):
        self.index_chunk = 0
        self.vorgänger = [0, 0, 0, 0]
        self.chunks = []
        self.random_x_first = 0
        self.floating_objects = self.load_floating_objects()
        self.ground_objects = self.load_ground_objects()
        self.add_chunk()
        self.add_chunk()
        self.obstacle_last_chunk = None

    def reset(self):
        self.chunks = []
        random.seed(time.time())
        self.add_chunk()
        self.add_chunk()

    def add_chunk(self):
        index = len(self.chunks)
        object_list = self.generate_objects()
        chunk = Chunk(len(self.chunks), object_list)
        self.chunks.append(chunk)

    def update(self, x_position):
        self.index_chunk = x_position // 1000
        # kommt als nächstes in neuen chunk
        if self.index_chunk + 1 == len(self.chunks):
            self.add_chunk()
            # generate new chunk
            # Bereich 5 4000 - 5000 (4 Chunks)

    def get_current_obstacles(self, x_position, player_width):
        index_chunk = x_position // 1000
        index_chunk2 = (x_position + player_width) // 1000
        obstacles = []

        if index_chunk == 0:
            obstacles += self.chunks[index_chunk].get_obstacles()

        elif index_chunk > 0:
            obstacles += self.chunks[index_chunk - 1].get_obstacles()
            obstacles += self.chunks[index_chunk].get_obstacles()

        if index_chunk != index_chunk2:  # player between 2 chunks
            obstacles += self.chunks[index_chunk2].get_obstacles()

        return obstacles

    def get_current_obstacles_view(self):
        obstacles = []
        if self.index_chunk == 0:
            obstacles += self.chunks[self.index_chunk].get_obstacles()
            obstacles += self.chunks[self.index_chunk + 1].get_obstacles()

        elif self.index_chunk > 0:
            obstacles += self.chunks[self.index_chunk - 1].get_obstacles()
            obstacles += self.chunks[self.index_chunk].get_obstacles()
            obstacles += self.chunks[self.index_chunk + 1].get_obstacles()

        return obstacles

    def load_floating_objects(self):
        floating_objects = []
        for obj in os.listdir(PATH_FLOATING_OBJECTS):
            img_path = os.path.join(PATH_FLOATING_OBJECTS, obj)
            img = Image.open(img_path)
            img_width, img_height = img.size
            floating_objects.append((img_path, img_width, img_height))
        return floating_objects

    def load_ground_objects(self):
        ground_objects = []
        for obj in os.listdir(PATH_GROUND_OBJECTS):
            img_path = os.path.join(PATH_GROUND_OBJECTS, obj)
            img = Image.open(img_path)
            img_width, img_height = img.size
            ground_objects.append((img_path, img_width, img_height, False))
        for obj in os.listdir(PATH_GROUND_DEATH):
            img_path = os.path.join(PATH_GROUND_DEATH, obj)
            img = Image.open(img_path)
            img_width, img_height = img.size
            ground_objects.append((img_path, img_width, img_height, True))
        return ground_objects

    def generate_objects(self):
        object_list = []
        space_available = True
        first = True
        # vorgänger[0]:x,vorgänger[1]:y,vorgänger[2]:width,vorgänger[3]:height
        while space_available:
            if first:
                random_x = self.random_x_first
                first = False
                # random_x = 0
            else:
                random_x = self.vorgänger[0] + self.vorgänger[2]

            random_x +=  random.randint(DISTANCE_MIN, DISTANCE_MAX)
            ground_floating_randint = random.randint(0, 9)

            if ground_floating_randint > 5:  # ground
                random_y = 0
                i = random.randint(0, len(self.ground_objects)-1)
                path, width, height, death = self.ground_objects[i]
            else:  # floating
                i = random.randint(0, len(self.floating_objects)-1)
                path, width, height = self.floating_objects[i]
                death = False
                y_min = self.vorgänger[1] - 90

                # self.vorgänger ist maximal 100 entfernt vom nächsten
                if y_min < - 600 + height + 100:  # aktueller darf nicht über das fenster kommen
                    y_min = - 600 + height + 100
                y_max = self.vorgänger[1] + 100
                if y_max > 0:
                    y_max = 0
                y_pred = random.randint(y_min, y_max)
                # print(y_pred)

                random_y = y_pred

            if random_x + width > 1000:
                current = [random_x, random_y, width, height]
                obstacle = Obstacle(current, path, death)
                object_list.append(obstacle)
                self.vorgänger = current[:]
                space_available = False
                self.random_x_first = random_x + width - 1000
            else:
                current = [random_x, random_y, width, height]
                object_list.append(Obstacle(current, path, death))
                self.vorgänger = current[:]
            if not space_available:
                self.vorgänger[0] = 0

        return object_list
