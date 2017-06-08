from abc import abstractmethod, ABCMeta


class Organism(metaclass=ABCMeta):

    def __init__(self, tile, world):
        self.tile = tile
        self.world = world
        self.isDead = False

    def kill(self):
        self.isDead = True

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        self.__strength = strength

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative):
        self.__initiative = initiative

    @property
    def world(self):
        return self.__world

    @world.setter
    def world(self, world):
        self.__world = world

    @property
    def tile(self):
        return self.__tile

    @tile.setter
    def tile(self, tile):
        self.__tile = tile

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def collision(self, attacker):
        if attacker.strength >= self.strength:
            self.world.kill_organism(self)
            self.kill()
        else:
            self.world.kill_organism(attacker)
            attacker.kill()
