import numpy as np
from util import *
from perso import *
import random


class Team:
    # Constructor

    def __init__(self):
        self.p = [Perso(), Perso(), Perso()]
        self.nom = "-"
        self.victoires = 0
        self.defaites = 0
        self.sommeVie = 0
        self.sommeDeg = 0
        self.sommeTours = 0
        self.fitness = 0
        self.ALPHA = 1
        self.BETA = 1
        self.GAMMA = 1

    # Calcule baseStats pour chaque personnage
    def getReady(self):
        for i in range(len(self.p)):
            self.p[i].reset()

    def shuffle(self):
        for i in range(len(self.p)):
            self.p[i].classe = random.randint(0, 6)

    def dispFitness(self):
        print(str(self.fitness) + " - " + self.nom +
              " (" + classes[self.p[0].classe] + " - " + classes[self.p[1].classe] +
              " - " + classes[self.p[2].classe] + ")")

    def fitnessStep(self, won, s, tours):
        if won:
            self.victoires += 1
        else:
            self.defaites += 1
        self.sommeVie += sum([self.p[i].battleStats[0] for i in range(3)]
                             ) / sum([self.p[i].stats[0] for i in range(3)])
        self.sommeDeg += s
        self.sommeTours += tours

    def calcFitness(self):
        self.fitness = ((1 + self.victoires) / (1 + self.defaites)) ** self.ALPHA \
                     * (self.sommeVie / self.sommeTours) ** self.BETA \
                     * (self.sommeDeg * self.sommeTours / (1 + self.defaites) ** 2) ** self.GAMMA
