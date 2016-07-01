import numpy as np
from util import *
from runes import *
import random
import re


class IA:

    def __init__(self, perso):
        self.p = perso
        self.rules = []

    def __call__(self, chars, nb, turn):
        if self.p.alive and self.p.idle == 0:

            # On interroge les portes logiques succesivement
            for rule in self.rules:
                if rule([chars, nb, turn]):
                    return rule.getAction([chars, nb, turn])

            # Fallback
            return [actionFallback]

        elif self.p.idle > 0:
            self.p.idle -= 1
            return []

    def setRule(n, rule):
        if len(runes) > n:
            self.rules[n] = rule

    def addRule(self,
                idPl=-1,
                idC1=-1,
                idC2=-1,
                idC=-1,
                idA=-1):

        if idPl == -1:
            idPl = int(random.random() * len(funLog))
        if idC1 == -1:
            idC1 = int(random.random() * len(idCond))
        if idC2 == -1:
            idC2 = int(random.random() * len(idCond))
        if idC == -1:
            idC = idCible[int(random.random() * len(idCible))]
        if idA == -1:
            idA = idAction[int(random.random() * len(idAction))]

        # Pour l'instant : seulement attaquer ou défendre

        if random.random() >= 0.5:
            idA = "swing"
        else:
            idA = "defend"

        if actionNeedCible[idA]:
            runeCible = Cible(idC, idC)
            runeAction = Action(idA, idA, True, runeCible)
        else:
            runeAction = Action(idA, idA, False)

        if idCond[idC1] in condParam100:
            param = int(random.random() * 100)
            runeCond1 = Cond(re.sub('X', str(param) + "%", idCond[idC1]), idC1, param)
        elif idCond[idC1] == "eachXTurn":
            param = int(random.random() * 4) + 2
            runeCond1 = Cond(re.sub('X', str(param), idCond[idC1]), idC1, param)
        else:
            runeCond1 = Cond(idCond[idC1], idC1)

        if idCond[idC2] in condParam100:
            param = int(random.random() * 100)
            runeCond2 = Cond(re.sub('X', str(param) + "%", idCond[idC2]), idC2, param)
        elif idCond[idC2] == "eachXTurn":
            param = int(random.random() * 4) + 2
            runeCond2 = Cond(re.sub('X', str(param), idCond[idC2]), idC2, param)
        else:
            runeCond2 = Cond(idCond[idC2], idC2)

        self.rules.append(PorteLogique(
            nomLog[idPl], idPl, runeAction, runeCond1, runeCond2))
