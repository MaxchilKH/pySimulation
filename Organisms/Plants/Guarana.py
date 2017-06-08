from Organisms.Plants.Plant import Plant


class Guarana(Plant):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 0

    def collision(self, attacker):
        attacker.strength += 3
        super().collision(attacker)

    def draw(self):
        return "#ef3300"