from pySimulation.Organisms.Animals.Animal import Animal


class CyberSheep(Animal):

    def draw(self):
        return "#afaeac"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 4
        self.initiative = 4

    def action(self):
        hogweeds = self.world.get_hogweed()

        hogweed = min([])

        super().action()


