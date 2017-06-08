from abc import ABCMeta
from pySimulation.Organisms.Organism import Organism
import random


class Animal(Organism, metaclass=ABCMeta):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.canMove = True

    def action(self):
        moves = self.world.get_neighbours(self.tile)
        tile = random.choice(moves)

        self.move(tile)

    @property
    def canMove(self):
        return self.__canMove

    @canMove.setter
    def canMove(self, can):
        self.__canMove = can

    def move(self, tile):
        if tile.organism is not None:
            tile.organism.collision(self)

        if not self.isDead and self.canMove:
            self.tile.organism = None
            self.tile = tile
            tile.organism = self

        self.canMove = True

    def collision(self, attacker):
        if type(self) is type(attacker):
            tile = self.world.get_free_neighbours(self.tile)
            attacker.canMove = False

            if not tile:
                return

            self.world.add_organism(self.__class__(random.choice(tile), self.world))
            return

        super().collision(attacker)

