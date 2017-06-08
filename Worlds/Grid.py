from Worlds.Tile import Tile


class Grid(Tile):

    def __init__(self, pos, world, org):
        super().__init__(pos, world)
        size = 30
        x, y = pos
        self.organism = org
        self.shape = [x*size, y*size, x*size + size, y*size, x*size + size, y*size+size, x*size, y*size+size]

    def get_neighbours(self) -> set:
        x, y = self.position
        return {(x+1, y), (x, y+1), (x-1, y), (x, y-1)}
