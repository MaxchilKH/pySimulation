from pySimulation.Organisms.Animals.Animal import Animal
import random


class Turtle(Animal):

    def draw(self):
        return "#91ad2e"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 2
        self.initiative = 1

    def action(self):
        moves = self.world.get_neighbours(self.tile)

        if not moves:
            return
        if random.randint(0, 100) >= 75:
            self.move(random.choice(moves))

    def collision(self, attacker):
        if attacker.strength < 5 and not isinstance(attacker, Turtle):
            attacker.canMove = False
            return

        super().collision(attacker)
