from Model.world.chunk import Chunk
from Model.Entity.obstacle import Obstacle

class World:
    def __init__(self):
        self.loaded_chunks = 0
        self.index_chunk = 0
        self.chunks = []
        self.add_chunk(0)
        self.add_chunk(1)


    def add_chunk(self, difficulty):
        object_list = [Obstacle((300, -90, 200, 50)), Obstacle((400, -270, 200, 50)), Obstacle((700, -100, 100, 50))] # fat jonas
        chunk = Chunk(len(self.chunks), difficulty, object_list)
        self.chunks.append(chunk)
        
    def update(self, x_position):
        self.index_chunk = x_position // 1000
        if self.index_chunk + 1 == len(self.chunks):
            self.add_chunk(0)
            #generate new chunk
            # Bereich 5 4000 - 5000 (4 Chunks)
            
    def get_current_obstacles(self, x_position, player_width):
        index_chunk = x_position // 1000
        index_chunk2 = (x_position + player_width) // 1000
        object_list = self.chunks[index_chunk].get_obstacles()

        if index_chunk != index_chunk2: # player between 2 chunks
            object_list += self.chunks[index_chunk2].get_obstacles()
            
        return object_list

    def get_current_obstacles_view(self):
        obstacles = []
        if self.index_chunk == 0:
            obstacles += self.chunks[self.index_chunk].get_obstacles()
            obstacles += self.chunks[self.index_chunk + 1].get_obstacles()
            
        elif self.index_chunk > 0:
            obstacles += self.chunks[self.index_chunk - 1].get_obstacles()
            obstacles += self.chunks[self.index_chunk].get_obstacles()
            obstacles += self.chunks[self.index_chunk + 1].get_obstacles()
        # print(obstacles)
        # print('\n\n')
        return obstacles
