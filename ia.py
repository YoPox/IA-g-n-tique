import numpy as np
from util import *
from perso import *
from team import *
from battle import *
from turn import *
import random
import time

# Constantes
NB = 100  # Nombre de teams
DV = 10
MU = 0.05  # Pourcentage de mutation
TN = 5  # Nombre de tournois
AL = NB / 50  # Nombre d'équipes aléatoires ajoutées au repeuplement
GN = 1  # Nombre de générations

# On crée les teams de la génération 1
teams = [Team() for i in range(NB)]

# On choisit les persos aléatoirement
for t in teams:
    t.shuffle()
    t.getReady()

# On va jusqu'à GN générations
for a in range(GN):

    print("GÉNÉRATION " + str(a))

    for t in range(TN):
        print("—————")
        alea = random.sample(range(NB), NB)
        partitions = [alea[DV * j:DV * (j + 1)] for j in range(NB // DV)]
        for i in range(NB // DV):
            print(partitions[i])
            tmt = Turnament([teams[k] for k in partitions[i]])
            tmt.process()
