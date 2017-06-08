from Organisms.Animals.Animal import Animal
import random


class Antilope(Animal):

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 4
        self.initiative = 4

    def draw(self):
        return "#875409"

    def action(self):
        moves = set()
        moves.update(self.world.get_neighbours(self.tile))
        moves.update([tile for a in moves for tile in self.world.get_neighbours(a)])

        moves.remove(self.tile)

        if not moves:
            return

        moves = [tile for tile in moves]
        self.move(random.choice(moves))

    def collision(self, attacker):
        if random.randint(0, 100) >= 50 or isinstance(attacker, Antilope):
            super().collision(attacker)
        else:
            moves = self.world.get_free_neighbours(self.tile)

            if not moves:
                return

            self.world.comment("Antylopa ran from {}\n".format(type(attacker).__name__))

            self.move(random.choice(moves))