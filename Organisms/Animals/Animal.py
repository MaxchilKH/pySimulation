from abc import ABCMeta
from pySimulation.Organisms.Organism import Organism
import random


class Animal(Organism, metaclass=ABCMeta):

    def __init__(self, tile):
        super().__init__(tile)
        self.canMove = True

    def action(self):
        self.canMove = True
        moves = self.world.get_neighbours(self)
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
            tile.organism = self
