import numpy as np
from util import *
from ia import *
from equip import *
import random


class Perso:
    # Constructor

    def __init__(self):
        self.classe = 0
        self.ia = IA(self)
        self.baseStats = [50, 100, 5, 5, 5, 5, 5]
        self.arme = Equip("Poings", 0, buffs=[0, 5])
        self.equip = []
        self.baseWeapon = 10
        self.buffs = []
        # HP - MP - ATK - WIS - DEF - SPD - LCK
        self.stats = [0, 0, 0, 0, 0, 0, 0]
        self.battleStats = [0, 0, 0, 0, 0, 0, 0]
        self.alive = True
        self.idle = 0
        self.overrideAction = []
        self.stateNow = []
        self.stateLast = []

    def __call__(self):
        print("—————————————————")
        print(classes[self.classe])
        for rule in self.ia.rules:
            rule.dispRule()
        print("—————————————————")

    # Stats normales d'un début de tour et applique les buffs
    # du tour
    def updateStats(self):
        # On reset les stats sur self.stats
        for i in range(2, len(self.stats)):
            self.battleStats[i] = self.stats[i]
        # On applique les buffs
        for i in range(len(self.buffs)):
            self.battleStats[self.buffs[i][0]] += self.buffs[i][1]
            self.buffs[i][2] -= 1
            if (self.buffs[i][2] <= 0):
                del self.buffs[i]
        # Actions du tour précédent
        self.stateLast = [a for a in self.stateNow]
        self.stateNow = []

    # Reset les stats
    def calcStats(self):
        self.baseStats = np.copy(classes_stats[self.classe])
        for i in range(len(self.stats)):
            self.stats[i] = self.baseStats[i]
            for j in [e for e in self.equip if e.cat != 2]:
                self.stats += np.array(e.stats)
            self.battleStats[i] = self.baseStats[i]

    # Renvoie l'action du tour
    def getIA(self, chars, nb, turn):
        if len(self.overrideAction):
            ia = self.overrideAction[0]
            self.overrideAction = []
            return ia
        ia = self.ia(chars, nb, turn)
        if ia == None or len(ia) == 0:
            return []
        else:
            return [nb] + ia

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
