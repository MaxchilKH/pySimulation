from pySimulation.Organisms.Plants.Plant import Plant


class Grass(Plant):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 0

    def draw(self):
        return "#009928"
