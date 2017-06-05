from pySimulation.Organisms.Animals.Animal import Animal


class Wolf(Animal):

    def draw(self):
        pass

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 9
        self.initiative = 5
