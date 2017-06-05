from pySimulation.Organisms.Animals.Animal import Animal
import random


class Antilope(Animal):

    def draw(self):
        pass

    def __init__(self, tile):
        super().__init__(tile)
        self.strength = 4
        self.initiative = 4

    def action(self):
        moves = self.world.get_neighbours(self.tile)
        moves.update([tile for a in moves for tile in self.world.get_neighbours(a)])

        if not moves:
            return

        self.move(random.choice(moves))

    def collision(self, attacker):
        if random.randint(0, 100) >= 50:
            super().collision(attacker)
        else:
            moves = self.world.get_free_neighbours(self.tile)

            if not moves:
                return
            
            self.move(random.choice(moves))