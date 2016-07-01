import random

classes = ["Guerrier",
           "Paladin",
           "Ninja",
           "Mage",
           "Prêtre",
           "Flutiste",
           "Pistolero"]

classes_stats = [[100, 15, 10, 4, 6, 8, 5],
                 [120, 12, 5, 2, 12, 5, 5],
                 [90, 25, 6, 3, 4, 15, 5],
                 [85, 85, 4, 12, 5, 8, 5],
                 [100, 110, 2, 8, 6, 8, 5],
                 [85, 85, 3, 6, 8, 12, 5],
                 [100, 65, 7, 7, 5, 7, 5]]

funLog = [(lambda x: x),
          (lambda x: not x),
          (lambda x, y: x and y),
          (lambda x, y: x or y),
          (lambda x, y: (x or y) and (not(x and y))),
          (lambda x, y: not (x and y)),
          (lambda x, y: not (x or y)),
          (lambda x, y: not ((x or y) and (not(x and y))))]

nomLog = ["ID",
          "NOT",
          "AND",
          "OR",
          "XOR",
          "NAND",
          "NOR",
          "NXOR"]

idCond = ["eachTurn",
          "eachXTurn",
          "hitLast",
          "hitPLast",
          "hitMLast",
          "healedLast",
          "killedLast",
          "hasHitLast",
          "hasHitPLast",
          "hasHitMLast",
          "charge",
          "chargeP",
          "chargeM",
          "hasHealedLast",
          "selfHealedLast",
          "allyHealedLast",
          "hasBuffedLast",
          "hasBuffedSelfLast",
          "hasBuffedAllyLast",
          "hasBuffedEnnemyLast",
          "warmed",
          "watches",
          "defends",
          "protects",
          "waits",
          "hasNegBuff",
          "hasPosBuff",
          "moreThanXLife",
          "lessThanXLife",
          "moreThanXMana",
          "lessThanXMana"]

condParam100 = ["moreThanXLife",
                "lessThanXLife",
                "moreThanXMana",
                "lessThanXMana"]

idCible = ["allMostHPMax",
           "allLessHPMax",
           "allyMostHPMax",
           "allyLessHPMax",
           "ennMostHPMax",
           "ennLessHPMax",
           "allMostHP",
           "allLessHP",
           "allyMostHP",
           "allyLessHP",
           "ennMostHP",
           "ennLessHP",
           "allMostMPMax",
           "allLessMPMax",
           "allyMostMPMax",
           "allyLessMPMax",
           "ennMostMPMax",
           "ennLessMPMax",
           "allMostMP",
           "allLessMP",
           "allyMostMP",
           "allyLessMP",
           "ennMostMP",
           "ennLessMP",
           "allMostATK",
           "allLessATK",
           "allyMostATK",
           "allyLessATK",
           "ennMostATK",
           "ennLessATK",
           "allMostWSD",
           "allLessWSD",
           "allyMostWSD",
           "allyLessWSD",
           "ennMostWSD",
           "ennLessWSD",
           "allMostDEF",
           "allLessDEF",
           "allyMostDEF",
           "allyLessDEF",
           "ennMostDEF",
           "ennLessDEF",
           "allMostSPD",
           "allLessSPD",
           "allyMostSPD",
           "allyLessSPD",
           "ennMostSPD",
           "ennLessSPD",
           "self",
           "ally",
           "enn",
           "allBuffed",
           "allBuffedPos",
           "allBuffedNeg",
           "allyBuffed",
           "allyBuffedPos",
           "allyBufedNeg",
           "ennBuffed",
           "ennBuffedPos",
           "ennBuffedNeg"]

idAction = ["swing",
            "strike",
            "charge",
            "readSpell1",
            "readSpell2",
            "singSpell1",
            "singSpell2",
            "chargeSpell1",
            "chargeSpell2",
            "protect",
            "defend",
            "shell",
            "watch",
            "warm",
            "wait"]

actionNeedCible = {
    "swing": True,
    "strike": True,
    "charge": False,
    "readSpell1": True,
    "readSpell2": True,
    "singSpell1": True,
    "singSpell2": True,
    "chargeSpell1": True,
    "chargeSpell2": True,
    "protect": True,
    "defend": False,
    "shell": False,
    "watch": False,
    "warm": False,
    "wait": False}

actionFallback = "wait"

# Permet de lire un idCible


def getParams(idCble):
    stat = 0
    crit = "rand"
    cible = "any"
    if "all" in idCble:
        cible = "all"
    if "ally" in idCble:
        cible = "ally"
    elif "enn" in idCble:
        cible = "enn"
    if "Most" in idCble:
        cible = "most"
    elif "Less" in idCble:
        cible = "less"
    if "HP" in idCble:
        stat = 0
    elif "MP" in idCble:
        stat = 1
    elif "ATK" in idCble:
        stat = 2
    elif "WSD" in idCble:
        stat = 3
    elif "DEF" in idCble:
        stat = 4
    elif "SPD" in idCble:
        stat = 5
    return [stat, crit, cible]

# Sélectionne un perso selon une stat actuelle


def selectChar(context, stat, crit, cible):
    iTable = []
    if cible == "any":
        iTable += range(6)
    elif cible == "ally":
        iTable += range(context[1] // 3 * 3, context[1] // 3 * 3 + 3)
    else:
        iTable += range((1 - context[1] // 3) * 3,
                        (1 - context[1] // 3) * 3 + 3)
    if crit == "most":
        return iTable.sort(key=lambda x: -context[0][x].battleStats[stat])[0]
    if crit == "less":
        return iTable.sort(key=lambda x: context[0][x].battleStats[stat])[0]
    if crit == "rand":
        random.shuffle(iTable)
        return iTable[0]

# Sélectionne un perso selon une stat max


def selectCharBase(context, stat, crit, cible):
    iTable = []
    if cible == "any":
        iTable += range(6)
    elif cible == "ally":
        iTable += range(context[1] // 3 * 3, context[1] // 3 * 3 + 3)
    else:
        iTable += range((1 - context[1] // 3) * 3,
                        (1 - context[1] // 3) * 3 + 3)
    if crit == "most":
        return iTable.sort(key=lambda x: -context[0][x].stats[stat])[0]
    if crit == "less":
        return iTable.sort(key=lambda x: context[0][x].stats[stat])[0]

# Sélectionne un perso selon un buff


def selectCharBuffed(context, crit, cible):
    iTable = []
    if cible == "any":
        tab = [i for i in range(6) if len(context[0][i].buffs) != 0]
        random.shuffle(tab)
        iTable += tab
    elif cible == "ally":
        tab = [i for i in range(
            context[1] // 3 * 3, context[1] // 3 * 3 + 3) if len(context[0][i].buffs) != 0]
        random.shuffle(tab)
        iTable += tab
    else:
        tab = [i for i in range((1 - context[1] // 3) * 3, (1 -
                                                            context[1] // 3) * 3 + 3) if len(context[0][i].buffs) != 0]
        random.shuffle(tab)
        iTable += tab

    if len(iTable) == 0:  # Aucune cible
        return -1

    if crit == "any":
        return iTable[0]

    elif crit == "pos":
        for i in iTable:
            if max(context[0][i].buffs[:, 1] > 0):
                return i

    elif crit == "neg":
        for i in iTable:
            if min(context[0][i].buffs[:, 1] < 0):
                return i

    return -1
