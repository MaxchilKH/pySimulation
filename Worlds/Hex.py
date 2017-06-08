from pySimulation.Worlds.Tile import Tile


class Hex(Tile):

    def __init__(self, pos, world, org):
        super().__init__(pos, world)
        rad = 20
        h = 0.85 * 20
        x, y = pos

        yoff = (2 * y + x % 2) * h
        xoff = x * 1.5 * rad

        self.organism = org
        self.shape = [xoff, h+yoff,
                      rad / 2 + xoff, yoff,
                      3*rad/2 + xoff, yoff,
                      rad*2 + xoff, h + yoff,
                      3*rad/2 + xoff, h*2 + yoff,
                      rad/2 + xoff, h*2 + yoff]

    def get_neighbours(self) -> set:
        x, y = self.position
        if x % 2 == 0:
            return {(x - 1, y-1), (x, y-1), (x+1, y - 1), (x+1, y),
                    (x, y+1), (x-1, y)}
        else:
            return {(x-1, y), (x, y-1), (x+1, y), (x + 1, y+1),
                    (x, y+1), (x - 1, y + 1)}
