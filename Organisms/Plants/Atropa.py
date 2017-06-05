from pySimulation.Organisms.Plants.Plant import Plant


class Atropa(Plant):

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 99

    def collision(self, attacker):
        self.world.kill_organism(self)
        self.world.kill_organism(attacker)
