from pySimulation.Organisms.Plants.Plant import Plant


class Guarana(Plant):

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 0

    def collision(self, attacker):
        attacker.strength += 3
        super().collision(attacker)
