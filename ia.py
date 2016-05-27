import numpy as np
from util import *
from perso import *
from team import *
from battle import *
import random
import time

stats = [0, 0]

for a in range(500):

    t1 = Team()
    t2 = Team()
    t1.shuffleP()
    t1.getReady()
    t1.name = "Team aléatoire 1"
    t2.shuffleP()
    t2.getReady()
    t2.name = "Team aléatoire 2"

    teams1 = [t1, t2]

    b = Battle([teams1[0].p[0], teams1[0].p[1], teams1[0].p[2],
                teams1[1].p[0], teams1[1].p[1], teams1[1].p[2]])
    b.processBattle()

    stats[b.winner] += 1

    teams1[0].getReady()
    teams1[1].getReady()

    b2 = Battle([teams1[1].p[0], teams1[1].p[1], teams1[1].p[2],
                teams1[0].p[0], teams1[0].p[1], teams1[0].p[2]])
    b2.processBattle()
    stats[1 - b2.winner] += 1

print(stats)
