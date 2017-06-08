from Organisms.Plants.Plant import Plant


class Atropa(Plant):

    def draw(self):
        return "#2a127a"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 99

    def collision(self, attacker):
        self.world.kill_organism(self)
        self.world.kill_organism(attacker)
