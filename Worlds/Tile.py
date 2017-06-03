from abc import ABCMeta, abstractmethod


class Tile(metaclass=ABCMeta):

    def __init__(self, pos):
        self.position = pos
        self.organism = None
        self.shape = list()

    @abstractmethod
    def get_neighbours(self):
        pass

    @abstractmethod
    def check_click(self):
        pass

    @property
    def organism(self):
        return self.__organism

    @organism.setter
    def organism(self, org):
            self.__organism = org

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        self.__position = pos

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, sh):
        self.__shape = sh