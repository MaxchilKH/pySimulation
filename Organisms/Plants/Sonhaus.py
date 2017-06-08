from pySimulation.Organisms.Plants.Plant import Plant


class Sonhaus(Plant):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 0

    def action(self):
        super().action()
        super().action()
        super().action()

    def draw(self):
        return "#eeff00"
