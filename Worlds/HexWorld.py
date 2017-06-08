from pySimulation.Worlds.AbstractWorld import AbstractWorld
from pySimulation.Worlds.Hex import Hex


class HexWorld(AbstractWorld):

    def __init__(self, w, h, master):
        super().__init__(w, h, master)
        self.map = {(i, j): Hex((i, j), self, None) for i in range(w) for j in range(h)}
        self.draw_map()
