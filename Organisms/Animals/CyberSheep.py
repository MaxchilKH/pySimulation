from pySimulation.Organisms.Animals.Animal import Animal


class CyberSheep(Animal):

    def draw(self):
        pass

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 4
        self.initiative = 4
