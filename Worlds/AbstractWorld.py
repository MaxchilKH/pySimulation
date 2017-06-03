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
        pass

    def kill_organism(self, org):
        pass

    def add_organism(self):
        pass
