from pySimulation.Organisms.Animals.Animal import Animal


class Sheep(Animal):

    def draw(self):
        return "#fff"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 4
        self.initiative = 4
