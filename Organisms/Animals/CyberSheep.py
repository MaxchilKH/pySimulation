from Organisms.Animals.Animal import Animal
import math

class CyberSheep(Animal):

    def draw(self):
        return "#afaeac"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 4
        self.initiative = 4

    def action(self):
        hogweeds = self.world.get_hogweed()
        if not hogweeds:
            super().action()
            return

        hogweedspos = [org.tile.position for org in hogweeds]



        x, y = self.tile.position

        hx, hy = min([(math.sqrt((x - hx)**2 + (y - hy)**2), (hx, hy)) for hx, hy in hogweedspos])[1]

        if hx > x:
            self.move(self.world.map[(x+1, y)])
        elif hx < x:
            self.move(self.world.map[(x-1, y)])
        elif hy > y:
            self.move(self.world.map[(x, y + 1)])
        elif hy < y:
            self.move(self.world.map[(x, y - 1)])






