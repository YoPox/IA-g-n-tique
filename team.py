import numpy as np
from util import *
from perso import *
import random


class Team:
    # Constructor

    def __init__(self):
        self.p = [Perso(), Perso(), Perso()]
        self.nom = "-"

    # Calcule baseStats pour chaque personnage
    def getReady(self):
        for i in range(len(self.p)):
            self.p[i].reset()

    def shuffleP(self):
        for i in range(len(self.p)):
            self.p[i].classe = random.randint(0, 6)
