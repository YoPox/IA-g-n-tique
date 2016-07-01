import random
from util import *


class Rune:

    def __init__(self, nom):
        self.nom = nom
        self.cout = 0

    def __call__(self, context):
        return []


class Cible(Rune):

    def __init__(self, nom, idCible):
        Rune.__init__(self, nom)
        self.idCible = idCible

    def __call__(self, context):
        # Cible = soi-même
        if self.idCible == "self":
            return context[1]
        # Cible = ally
        if self.idCible == "ally":
            tab = [i for i in range(context[1] // 3 * 3,
                                                    context[1] // 3 * 3 + 3) if i != context[1]]
            random.shuffle(tab)
            return tab[0]
        # Cible = enn
        if self.idCible == "enn":
            tab = [i for i in range((1 - context[1] // 3) * 3,
                                                    (1 - context[1] // 3) * 3 + 3) if i != context[1]]
            random.shuffle(tab)
            return tab[0]
        # On "lit" la cible
        stat, crit, cible = getParams(idCible)
        # On récupère la cible
        if "Max" in self.idCible:
            return selectCharBase(context, stat, crit, cible)
        elif "Buffed" in self.idCible:
            crit = "any"
            if "Pos" in self.idCible:
                crit = "pos"
            if "Neg" in self.idCible:
                crit = "neg"
            return selectCharBuffed(context, crit, cible)
        else:
            return selectChar(context, stat, crit, cible)

    def __str__(self):
        return self.nom


class Action(Rune):

    def __init__(self, nom, idAction, needCible, cible="self"):
        Rune.__init__(self, nom)
        self.idAction = idAction
        self.needCible = needCible
        self.cible = cible

    def __call__(self, context):
        if self.needCible:
            return [self.idAction, self.cible(context)]
        else:
            return [self.idAction]

    def __str__(self):
        return self.nom + " - " + str(self.cible)


class Cond(Rune):

    def __init__(self, nom, idCond, param=1):
        Rune.__init__(self, nom)
        self.idCond = idCond
        self.param = param

    def __call__(self, context):
        # La condition se résume à la présence d'un attribut
        if self.idCond >= 2 and self.idCond <= 27:
            return idCond[self.idCond] in context[0][context[1]].stateLast
        # eachTurn
        elif self.idCond == 0:
            return True
        # eachXTurn
        elif self.idCond == 1:
            return context[2] % self.param == 0
        # [more/less]ThanX[Life/Mana]
        elif self.idCond == 28:
            return context[0][context[1]].battleStats[0] / context[0][context[1]].stats[0] >= self.param
        elif self.idCond == 29:
            return context[0][context[1]].battleStats[0] / context[0][context[1]].stats[0] <= self.param
        elif self.idCond == 30:
            return context[0][context[1]].battleStats[1] / context[0][context[1]].stats[1] >= self.param
        elif self.idCond == 31:
            return context[0][context[1]].battleStats[1] / context[0][context[1]].stats[1] <= self.param

    def __str__(self):
        return self.nom

class PorteLogique(Rune):

    def __init__(self, nom, idLog, action, c1, c2=1):
        Rune.__init__(self, nom)
        # 0 : Id  ; 1 : Not  ; 2 : AND ; 3 : OR
        # 4 : XOR ; 5 : NAND ; 6 : NOR ; 7 : NXOR
        self.idLog = idLog
        self.action = action
        self.c1 = c1
        self.c2 = c2

    def __call__(self, context):
        if self.idLog >= 2:
            return funLog[self.idLog](self.c1(context), self.c2(context))
        else:
            return funLog[self.idLog](self.c1(context))

    def getAction(self, context):
        return self.action(context)

    def dispRule(self):
        if self.idLog >= 2:
            print(self.nom + " ( " + str(self.c1) + " " + str(self.c2) + " ) " + str(self.action))
        else:
            print(self.nom + " ( " + str(self.c1) + " ) " + str(self.action))
