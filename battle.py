import numpy as np
from util import *
import math
import random


class Battle:
    # Constructor

    def __init__(self, chars):
        self.chars = chars
        self.turn = 1
        self.turnIA = []
        self.finished = False
        self.winner = 0

    def processBattle(self):
        for c in self.chars:
            c.calcStats()
        while not self.finished:
            self.doTurn()
            state = self.checkWin()
            if state[0]:
                self.finished = True
                self.winner = state[1]
            if self.turn > 999: # Combat trop long : match nul
                self.finished = True
                self.winner = -1

    def doTurn(self):

        self.chars[0].updateStats()
        self.chars[1].updateStats()
        self.chars[2].updateStats()
        self.chars[3].updateStats()
        self.chars[4].updateStats()
        self.chars[5].updateStats()

        charTable = []
        for i in range(len(self.chars)):
            charTable.append([i, self.chars[i].battleStats[5]])
        charTable.sort(key=lambda x: -x[1])

        self.turnIA = []

        for i in range(len(charTable)):
            t = self.chars[charTable[i][0]].getIA(
                self.chars, charTable[i][0], self.turn)
            if self.chars[charTable[i][0]].alive:
                self.turnIA.append(t)

        self.doAction()
        self.turn += 1

    def attack(self, a):
        if a[1] != None:
            if random.randint(0, 99) >= self.chars[a[0]].battleStats[6]:
                dmg = 0
                if a[2] == 0:
                    dmg = math.ceil(self.chars[a[0]].baseWeapon * (0.85 + (
                        self.chars[a[0]].battleStats[2] - self.chars[a[1]].battleStats[4]) / 100))
                    self.chars[a[1]].damage(dmg)
                else:
                    dmg = math.ceil(self.chars[a[0]].baseWeapon * (1.15 + (
                        self.chars[a[0]].battleStats[2] - self.chars[a[1]].battleStats[4]) / 100))
                    self.chars[a[1]].damage(dmg)
                self.chars[a[0]].stateNow += ["hasHitLast", "hasHitPLast"]
                self.chars[a[1]].stateNow += ["hitLast", "hitPLast"]
        else:
            pass # Pas de cible

    def spell(self, a):
        if a[1] != None:
            cost = 5
            if self.chars[a[0]].checkMana(cost):
                if a[2] == 0:
                    dmg = math.ceil(self.chars[a[0]].baseWeapon * (0.85 + (
                        self.chars[a[0]].battleStats[3] - self.chars[a[1]].battleStats[4]) / 100))
                    self.chars[a[1]].damage(dmg)
                else:
                    dmg = math.ceil(self.chars[a[0]].baseWeapon * (1.15 + (
                        self.chars[a[0]].battleStats[3] - self.chars[a[1]].battleStats[4]) / 100))
                    self.chars[a[1]].damage(dmg)
                self.chars[a[0]].stateNow += ["hasHitLast", "hasHitMLast"]
                self.chars[a[1]].stateNow += ["hitLast", "hitMLast"]
        else:
            pass # Pas de cible

    def defense(self, nb):
        self.chars[nb].battleStats[3] += 15
        self.chars[nb].stateNow += ["defends"]

    def shell(self, nb):
        self.chars[nb].battleStats[3] += 35
        self.chars[nb].buffs.append([3, 35, 1])
        self.chars[nb].idle = 1
        self.chars[nb].stateNow += ["defends"]

    def warms(self, nb):
        self.chars[nb].battleStats[3] += 5
        self.chars[nb].buffs.append([2, 20, 1])
        self.chars[nb].buffs.append([5, 20, 1])
        self.chars[nb].stateNow += ["warms"]

    def charge(self, a):
        self.chars[a[0]].overrideAction = ["strike", a[1]]
        self.chars[a[0]].buffs.append([1, 55, 1])
        self.chars[a[0]].stateNow += ["charge"]

    def watch(self, nb):
        self.chars[nb].battleStats[6] += 35
        self.chars[nb].buffs.append([6, 15, 1])
        self.chars[nb].stateNow += ["watches"]

    def protect(self, a):
        self.chars[a[0]].stateNow += ["protects"]
        pass

    def doAction(self):

        if len(self.turnIA) == 0 or self.checkWin()[0]:
            # self.onEnd()
            return 0
        ia = self.turnIA[0]
        if len(ia) > 0:
            if not self.chars[ia[0]].alive:
                del self.turnIA[0]
                self.doAction()
            else:
                if ia[1] == "swing":
                    self.attack([ia[0], ia[2], 0])
                elif ia[1] == "strike":
                    self.attack([ia[0], ia[2], 1])
                elif ia[1] == "warm":  # Warm Up
                    self.warms(ia[0])
                elif ia[1] == "readSpell1":  # Quick Spell
                    self.spell([ia[0], ia[2], 0])
                elif ia[1] == "singSpell1":  # Powerful Spell
                    self.spell([ia[0], ia[2], 1])
                elif ia[1] == "defend":  # Defense
                    self.defense(ia[0])
                elif ia[1] == "shell":  # Shell
                    self.shell(ia[0])
                elif ia[1] == "watch":  # Watch Out
                    self.watches(ia[0])
                elif ia[1] == "protect":  # Protect
                    self.protect([ia[0], ia[2]])
                elif ia[1] == "charge":  # Charge
                    self.charge([ia[0], ia[2]])

            if len(self.turnIA) > 0:
                del self.turnIA[0]
            self.doAction()

    def checkWin(self):
        if not self.chars[0].alive and not self.chars[1].alive and not self.chars[2].alive:
            return [True, 0]
        elif not self.chars[3].alive and not self.chars[4].alive and not self.chars[5].alive:
            return [True, 1]
        else:
            return [False]
