from pySimulation.Organisms.Animals.Animal import Animal
import random


class Fox(Animal):

    def draw(self):
        pass

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 3
        self.initiative = 7

    def action(self):
        moves = self.world.get_neighbours(self)
        moves = {tile for tile in moves if not (tile.organism is None or tile.organism.strength <= self.strength)}

        if not moves:
            return

        self.move(random.choice(moves))
