import numpy as np
from util import *
from perso import *
from team import *
from battle import *
from turn import *
import random
import time

# Constantes
NB = 1000  # Nombre de teams
MU = 0.05  # Pourcentage de mutation
TN = 20  # Nombre de tournois
AL = NB / 50  # Nombre d'équipes aléatoires ajoutées au repeuplement
GN = 100 # Nombre de générations

# On crée les teams de la génération 1
global teams
teams = [Team() for i in range(NB)]

# On choisit les persos aléatoirement
for t in teams:
    t.shuffle()
    t.getReady()

# On va jusqu'à GN générations
for a in range(GN):

    print("GÉNÉRATION " + str(a))

    # On fait les TN tournois
    for b in range(TN):
        tmt = Turnament(random.sample(range(NB), 100))
        tmt.process()
