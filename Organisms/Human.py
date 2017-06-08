from pySimulation.Organisms.Animals.Animal import Animal


class Human(Animal):

    def draw(self):
        return "red"

    def __init__(self, tile, world):
        super().__init__(tile, world)
        self.strength = 5
        self.initiative = 4
        self.powerActive = False
        self.possibleTiles = list()
        self.nt = 0
        self.powerTimer = 0

    def nextTile(self):
        self.possibleTiles = self.world.get_neighbours(self.tile)
        self.world.itemconfig(self.possibleTiles[self.nt].polygon, outline="black")
        self.nt = (self.nt + 1) % len(self.possibleTiles)
        self.world.itemconfig(self.possibleTiles[self.nt].polygon, outline="red")

    def prevTile(self):
        self.possibleTiles = self.world.get_neighbours(self.tile)
        self.world.itemconfig(self.possibleTiles[self.nt].polygon, outline="black")
        self.nt = ((self.nt - 1) % len(self.possibleTiles))
        self.world.itemconfig(self.possibleTiles[self.nt].polygon, outline="red")

    def action(self):
        if self.powerActive:
            kill = [tile.organism for tile in self.world.get_neighbours(self.tile) if tile.organism is not None]

            for org in kill:
                self.world.kill_organism(org)

            self.powerTimer += 1
            if self.powerTimer > 5:
                self.powerActive = False
        else:
            if self.powerTimer > 0:
                self.powerTimer -= 1

        print(self.possibleTiles, self.nt, self.tile)
        self.world.itemconfig(self.possibleTiles[self.nt].polygon, outline="black")
        self.move(self.possibleTiles[self.nt])

        self.nt = 0

    def activatePower(self):
        if self.powerActive or self.powerTimer > 0:
            return

        self.powerActive = True

