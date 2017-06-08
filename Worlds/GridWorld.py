from pySimulation.Worlds.AbstractWorld import AbstractWorld
from pySimulation.Worlds.Grid import Grid


class GridWorld(AbstractWorld):

    def __init__(self, w, h, master):
        super().__init__(w, h, master)
        self.map = {(i, j): Grid((i, j), self, None) for i in range(w) for j in range(h)}
        self.draw_map()
