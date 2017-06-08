from pySimulation.Organisms.Animals.Animal import Animal
import random


class Fox(Animal):

    def draw(self):
        return "#ff5000"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 3
        self.initiative = 7

    def action(self):
        moves = self.world.get_neighbours(self.tile)
        moves = [tile for tile in moves if (tile.organism is None or tile.organism.strength <= self.strength)]

        if not moves:
            return

        self.move(random.choice(moves))
