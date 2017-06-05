from abc import ABCMeta, abstractmethod


class AbstractWorld(metaclass=ABCMeta):

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.organisms = list()
        self.map = dict()

    def draw_gui(self):
        pass

    def tick(self):
        for org in self.organisms:
            org.action()

    def kill_organism(self, org):
        org.tile.organism = None
        self.organisms.remove(org)

    def add_organism(self, org):
        self.organisms.append(org)
        org.tile.organism = org

    def get_neighbours(self, t) -> set:
        return {self.map[tile] for tile in t.get_neighbours() if tile in self.map.keys()}

    def get_free_neighbours(self, t):
        return [tile for tile in self.get_neighbours(t) if tile.organism is not None]
