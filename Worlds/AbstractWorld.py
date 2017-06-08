from abc import ABCMeta, abstractmethod
from Organisms.Human import Human
from Organisms.Plants.Hogweed import Hogweed
import tkinter as tk


class AbstractWorld(tk.Canvas, metaclass=ABCMeta):

    def __init__(self, w, h, master):
        super().__init__(master=master)
        self.width = w
        self.height = h
        self.organisms = list()
        self.map = dict()
        self.human = None
        self.commenter = None

    def draw_map(self):
        for key, val in self.map.items():
            if val.organism is not None:
                color = val.organism.draw()
            else:
                color = "#adf6ff"
            val.polygon = self.create_polygon(val.shape, fill=color, outline="black")

    def tick(self):
        orgbefore = [org for org in self.organisms]
        for org in orgbefore:
            if not org.isDead:
                org.action()

    def add_human(self, tile):
        self.human = Human(tile, self)
        self.add_organism(self.human)

    def kill_organism(self, org):
        org.kill()
        if isinstance(org, Human):
            self.human = None

        org.tile.organism = None
        self.organisms.remove(org)

    def setcommentator(self, funcp):
        self.commenter = funcp

    def get_hogweed(self):
        return [org for org in self.organisms if isinstance(org, Hogweed)]

    def add_organism(self, org):
        self.organisms.append(org)
        org.tile.organism = org

    def get_neighbours(self, t) -> list:
        return [self.map[tile] for tile in t.get_neighbours() if tile in self.map.keys()]

    def get_free_neighbours(self, t):
        return [tile for tile in self.get_neighbours(t) if tile.organism is None]

    def comment(self, string):
        self.commenter(string)