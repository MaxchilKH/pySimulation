from abc import ABCMeta
from Organisms.Organism import Organism
import random


class Plant(Organism, metaclass=ABCMeta):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.initiative = 0

    def collision(self, attacker):
        super().collision(attacker)

    def action(self):
        if random.randint(0, 100) >= 10:
            return

        moves = self.world.get_free_neighbours(self.tile)

        if not moves:
            return

        self.world.add_organism(self.__class__(random.choice(moves), self.world))
