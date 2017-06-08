#!/usr/bin/env python

from pySimulation.Worlds.GridWorld import GridWorld
from pySimulation.Worlds.HexWorld import HexWorld
from pySimulation.Organisms.Animals.Sheep import Sheep
from pySimulation.Organisms.Animals.Wolf import Wolf
from pySimulation.Organisms.Animals.Antilope import Antilope
from pySimulation.Organisms.Animals.CyberSheep import CyberSheep
from pySimulation.Organisms.Animals.Turtle import Turtle
from pySimulation.Organisms.Animals.Fox import Fox
from pySimulation.Organisms.Plants.Atropa import Atropa
from pySimulation.Organisms.Plants.Sonhaus import Sonhaus
from pySimulation.Organisms.Plants.Grass import Grass
from pySimulation.Organisms.Plants.Guarana import Guarana
from pySimulation.Organisms.Plants.Hogweed import Hogweed
from pySimulation.Organisms.Human import Human
import tkinter as tk
from tkinter import filedialog
import pickle


class Simulation(tk.Frame):

    n = 5

    def click(self, event):
        if self.world.find_withtag(tk.CURRENT):
            for key, val in self.world.map.items():
                if val.polygon == self.world.find_withtag(tk.CURRENT)[0] and val.organism is None:
                    self.add_org_dialog(val)

    def key(self, event):
        if self.world.human is None:
            return

        if event.keysym == "Up" or event.keysym == "Right":
            self.world.human.nextTile()

        if event.keysym == "Down" or event.keysym == "Left":
            self.world.human.prevTile()

        if event.keysym == "space":
            self.world.human.activatePower()

    def __init__(self):
        tk.Frame.__init__(self, master=None)
        self.grid()
        self.canvasFrame = tk.Frame(self, bg="pink")
        self.world = HexWorld(5, 5, self.canvasFrame)
        self.create_widgets()

    def add_org_dialog(self, pos):
        def add():
            if x.get() == "Human":
                self.world.add_human(pos)
                choice.destroy()
                return

            org = globals()[x.get()](pos, self.world)
            self.world.add_organism(org)
            choice.destroy()

        x = tk.StringVar()
        choice = tk.Toplevel()

        options = [
            "Antilope",
            "CyberSheep",
            "Fox",
            "Sheep",
            "Turtle",
            "Wolf",
            "Atropa",
            "Grass",
            "Hogweed",
            "Guarana",
            "Sonhaus",
            "Human",
        ]

        for op in options:
            tk.Radiobutton(choice, text=op, variable=x, value=op, command=add).grid()

    def save_world(self):
        name = filedialog.asksaveasfilename()
        print(self.world.__class__)
        dict = {"class": self.world.__class__,
                "org": [(org.__class__, org.tile.position) for org in self.world.organisms],
                "w": self.world.width, "h":self.world.height}
        if self.world.human is not None:
            dict.update({"powAc": self.world.human.powerActive,
                         "powT": self.world.human.powerTimer})
        pickle.dump(dict, open(name, "w+b"))

    def load_world(self):
        name = filedialog.askopenfilename()
        dict = pickle.load(open(name, "rb"))
        self.canvasFrame.destroy()
        self.canvasFrame = tk.Frame(self, bg="pink")
        self.world = dict["class"](dict["w"], dict["h"], self.canvasFrame)

        for cls, pos in dict["org"]:
            if issubclass(cls, Human):
                self.world.add_human(self.world.map[pos])
                self.world.human.powerTimer = dict["powT"]
                self.world.human.powerActive = dict["powAc"]
                continue

            self.world.add_organism(cls(self.world.map[pos], self.world))

        self.create_widgets()

        print(dict)

    def new_game(self):
        pass

    def create_widgets(self):
        self.create_canvas()
        self.create_buttons()
        self.create_log()
        self.focus_set()
        self.bind("<Key>", self.key)

    def create_canvas(self):
        self.world.config(scrollregion=(0, 0, 1000, 1000), width=600, height=400, bg="green")
        scrollbarV = tk.Scrollbar(self.canvasFrame, orient=tk.VERTICAL, command=self.world.yview)
        scrollbarV.grid(column=1, row=0, sticky=tk.N+tk.S)
        scrollbarH = tk.Scrollbar(self.canvasFrame, orient=tk.HORIZONTAL, command=self.world.xview)
        scrollbarH.grid(column=0, row=1, sticky=tk.E + tk.W)

        self.world['xscrollcommand'] = scrollbarH.set
        self.world['yscrollcommand'] = scrollbarV.set

        self.canvasFrame.grid(column=1, row=0)
        self.world.grid(column=0, row=0)

        self.world.bind("<Button-1>", self.click)
        self.world.draw_map()

    def create_log(self):
        def comment(string):
            self.log.insert(tk.END, string)

        self.logFrame = tk.Frame(self)
        self.logFrame.grid(row=1, columnspan=2, sticky=tk.W+tk.E+tk.S+tk.N)
        self.log = tk.Text(self.logFrame)
        self.scrollLog = tk.Scrollbar(self.logFrame, orient=tk.VERTICAL, command=self.log.yview)
        self.scrollLog.grid(column=1, row=0, sticky=tk.N+tk.S)

        self.log['yscrollcommand'] = self.scrollLog.set

        self.log.grid(column=0, row=0)
        self.world.setcommentator(comment)

    def create_buttons(self):
        self.buttonsFrame = tk.Frame(self, padx=20, bg="red")
        self.buttonsFrame.grid(column=0, row=0)
        self.quitButton = tk.Button(self.buttonsFrame, text='Quit', command=self.quit)
        self.tickButton = tk.Button(self.buttonsFrame, text='Tick', command=self.world.tick)
        self.loadButton = tk.Button(self.buttonsFrame, text='Load', command=self.load_world)
        self.saveButton = tk.Button(self.buttonsFrame, text='Save', command=self.save_world)
        self.newButton = tk.Button(self.buttonsFrame, text='New', command=self.new_game)
        self.saveButton.grid()
        self.loadButton.grid()
        self.newButton.grid()
        self.tickButton.grid()
        self.quitButton.grid()

if __name__ == "__main__":
    app = Simulation()
    app.master.title('Sampelek')
    app.mainloop()
