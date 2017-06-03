from pySimulation.Organisms.Organism import Organism
import random

class Animal(Organism):

    def __init__(self, tile):
        super().__init__(tile)

    def action(self):
        moves = self.world.get_neighbours()


    def draw(self):
        super().draw()
