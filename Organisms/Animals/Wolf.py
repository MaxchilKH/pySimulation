from pySimulation.Organisms.Animals.Animal import Animal


class Wolf(Animal):

    def draw(self):
        return "#3a3733"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 9
        self.initiative = 5
