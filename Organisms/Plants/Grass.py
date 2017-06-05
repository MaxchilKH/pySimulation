from pySimulation.Organisms.Plants.Plant import Plant


class Grass(Plant):

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 0
