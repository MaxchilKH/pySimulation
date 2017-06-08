from pySimulation.Organisms.Plants.Plant import Plant
from pySimulation.Organisms.Animals.CyberSheep import CyberSheep
from pySimulation.Organisms.Animals.Animal import Animal


class Hogweed(Plant):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 10

    def action(self):
        kill = [tile.organism for tile in self.world.get_neighbours(self.tile) if
                isinstance(tile.organism, Animal) and not isinstance(tile.organism, CyberSheep)]

        for org in kill:
            self.world.kill_organism(org)

        super().action()

    def collision(self, attacker):
        self.world.kill_organism(self)
        if not isinstance(self, CyberSheep):
            self.world.kill_organism(attacker)

    def draw(self):
        return "#4fef00"
