from abc import ABCMeta, abstractmethod


class Tile(metaclass=ABCMeta):

    def __init__(self, pos, world):
        self.position = pos
        self.world = world
        self.polygon = None
        self.organism = None

    @abstractmethod
    def get_neighbours(self) -> set:
        pass

    @property
    def organism(self):
        return self.__organism

    @organism.setter
    def organism(self, org):
        if org is not None:
            color = org.draw()
        else:
            color = "#adf6ff"

        self.world.itemconfig(self.polygon, fill=color)
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