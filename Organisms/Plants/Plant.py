from abc import ABCMeta
from pySimulation.Organisms.Organism import Organism
import random


class Plant(Organism, metaclass=ABCMeta):

    def __init__(self, tile):
        super().__init__(tile)
        self.initiative = 0

    def collision(self, attacker):
        super().collision(attacker)
        self.world.kill_organism(self)

    def action(self):
        if random.randint(0, 100) >= 25:
            return

        moves = self.world.get_free_neighbours(self.tile)

        if not moves:
            return

        self.world.add_organism(self.__class__(random.choice(moves), self.world))
