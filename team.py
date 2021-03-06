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

    def __call__(self):
        print("—————————————————")
        print(self.fitness)
        print(str(self.victoires / (self.victoires + self.defaites) * 100) + " %")
        for perso in self.p:
            perso()

    # Calcule baseStats pour chaque personnage
    def getReady(self):
        for i in range(len(self.p)):
            self.p[i].reset()

    def shuffle(self):
        for i in range(len(self.p)):
            self.p[i].classe = random.randint(0, 6)
            for a in range(5):
                self.p[i].ia.addRule()

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
        self.fitness = ((self.victoires) / (self.victoires + self.defaites)) ** self.ALPHA \
            * (self.sommeVie / self.sommeTours) ** self.BETA \
            * (self.sommeDeg * self.sommeTours / (1 + self.defaites) ** 2) ** self.GAMMA
