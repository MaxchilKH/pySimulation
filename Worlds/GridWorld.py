from pySimulation.Worlds.AbstractWorld import AbstractWorld
from pySimulation.Worlds.Grid import Grid


class GridWorld(AbstractWorld):

    def __init__(self, w, h):
        super().__init__(w, h)
        self.map = {(i, j): Grid((i, j), None) for i in range(w) for j in range(h)}
