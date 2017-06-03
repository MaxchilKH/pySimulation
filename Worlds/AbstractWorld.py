from abc import ABCMeta, abstractmethod


class AbstractWorld(metaclass=ABCMeta):

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.organisms = list()
        self.mapa = dict()

    def draw_gui(self):
        pass

    def tick(self):
        pass

    def kill_organism(self, org):
        pass

    def add_organism(self, org):
        pass

    def get_neighbours(self, org):
        return [tile for tile in org.tile.get_neighbours() if tile in self.mapa.keys()]

    def get_free_neigbours(self, org):
        return [tile for tile in self.get_neighbours(org) if tile.organism is not None]
