from pySimulation.Organisms.Plants.Plant import Plant
from pySimulation.Organisms.Animals.CyberSheep import CyberSheep
from pySimulation.Organisms.Animals.Animal import Animal


class Hogweed(Plant):

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 10

    def action(self):
        kill = [tile.organism for tile in self.world.get_free_neighbours(self.tile) if
                isinstance(tile.organism, Animal) and not isinstance(tile.organism, CyberSheep)]

        for org in kill:
            self.world.kill_organism(org)

        super().action()

    def collision(self, attacker):
        self.world.kill_organism(self)
        if not isinstance(self, CyberSheep):
            self.world.kill_organism(attacker)
