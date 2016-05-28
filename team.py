import numpy as np
from util import *
from perso import *
import random


class Team:
    # Constructor

    def __init__(self):
        self.p = [Perso(), Perso(), Perso()]
        self.nom = "-"
        self.win = 0
        self.lose = 0
        self.fitness = 0

    # Calcule baseStats pour chaque personnage
    def getReady(self):
        for i in range(len(self.p)):
            self.p[i].reset()

    def shuffle(self):
        for i in range(len(self.p)):
            self.p[i].classe = random.randint(0, 6)
