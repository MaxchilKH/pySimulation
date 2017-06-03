from pySimulation.Worlds.Tile import Tile


class Grid(Tile):

    def __init__(self, pos, org):
        super().__init__(pos)
        self.organism = org

    def get_neighbours(self):
        x, y = self.position
        return {(x+1, y), (x, y+1), (x-1, y), (x, y-1)}

    def check_click(self):
        pass
