from pySimulation.Organisms.Plants.Plant import Plant


class Sonhaus(Plant):

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 0

    def action(self):
        super().action()
        super().action()
        super().action()
