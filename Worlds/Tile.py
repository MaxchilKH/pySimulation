from abc import ABCMeta, abstractmethod


class Tile(metaclass=ABCMeta):

    def __init__(self, pos):
        self.position = pos
        self.shape = list()

    @abstractmethod
    def get_neighbours(self):
        pass

    @abstractmethod
    def check_click(self):
        pass
