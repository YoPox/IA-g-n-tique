import numpy as np
from util import *
import random


class Perso:
    # Constructor

    def __init__(self):
        self.classe = 0
        self.rules = [[], [], [], [], []]
        self.baseStats = [50, 100, 5, 5, 5, 5, 5]
        self.equip = []
        self.buffs = []
        # HP - MP - ATK - WIS - DEF - SPD - LCK
        self.stats = [0, 0, 0, 0, 0, 0, 0]
        self.battleStats = [0, 0, 0, 0, 0, 0, 0]
        self.alive = True
        self.idle = 0
        self.baseWeapon = 10

    # Stats normales d'un début de tour et applique les buffs
    # du tour
    def updateStats(self):
        for i in range(2, len(self.stats)):
            self.battleStats[i] = self.stats[i]
        for i in range(len(self.buffs)):
            self.battleStats[self.buffs[i][0]] += self.buffs[i][1]
            self.buffs[i][2] -= 1
            if (self.buffs[i][2] <= 0):
                del self.buffs[i]

    # Reset les stats
    def calcStats(self):
        self.baseStats = np.copy(classes_stats[self.classe])
        for i in range(len(self.stats)):
            for j in range(len(self.equip)):
                pass
                # TODO: Equip
            self.stats[i] = self.baseStats[i]
            self.battleStats[i] = self.baseStats[i]

    # Renvoie l'action du tour
    def getIA(self, chars, nb, turn):
        if self.alive and self.idle == 0:
            # TODO: Implement proper IA
            c1 = random.randint(0, 2) + 3 - 3 * int(nb / 3)
            while not chars[c1].alive:
                c1 = random.randint(0, 2) + 3 - 3 * int(nb / 3)
            # c2 = random.randint(0, 2) + 3 * int(nb / 3)
            # while (c2 == nb):
            #     c2 = random.randint(0, 2) + 3 * int(nb / 3)
            return [nb, random.randint(0, 9), c1]
        elif self.idle > 0:
            self.idle -= 1
            return []

    def damage(self, dmg):
        if self.battleStats[0] - dmg > 0:
            self.battleStats[0] -= dmg
        else:
            self.battleStats[0] = 0
            self.alive = False

    def checkMana(self, nb):
        if self.battleStats[1] - nb >= 0:
            self.battleStats[1] -= nb
            return True
        return False

    def reset(self):
        self.alive = True
        self.idle = 0
        self.buffs = []
        self.calcStats()
