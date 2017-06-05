from pySimulation.Organisms.Animals.Animal import Animal
import random


class Turtle(Animal):

    def draw(self):
        pass

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 2
        self.initiative = 1

    def action(self):
        moves = self.world.get_neighbours(self)

        if not moves:
            return
        if random.randint(0, 100) >= 75:
            self.move(random.choice(moves))

    def collision(self, attacker):
        if attacker.strength < 5 and not isinstance(attacker, Turtle):
            attacker.canMove = False
            return

        super().collision(attacker)
