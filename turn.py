import numpy as np
from util import *
from battle import *
import math
import random


class Turnament:
    # Constructor

    def __init__(self, teams):
        self.teams = teams

    def process(self):

        # COMBATS EN N(N-1)

        for a in range(len(self.teams)):
            for b in range(len(self.teams)):
                if a != b:

                    fitness = 0

                    self.teams[a].getReady()
                    self.teams[b].getReady()

                    # Manche 1
                    btl = Battle(self.teams[a].p + self.teams[b].p)
                    btl.processBattle()

                    if btl.winner >= 0: # En cas de match nul
                        self.teams[a].fitnessStep(btl.winner, sum([self.teams[b].p[i].battleStats[0] for i in range(3)])/sum([self.teams[b].p[i].stats[0] for i in range(3)]), btl.turn)
                        self.teams[b].fitnessStep(1 - btl.winner, sum([self.teams[a].p[i].battleStats[0] for i in range(3)])/sum([self.teams[a].p[i].stats[0] for i in range(3)]), btl.turn)

                    self.teams[a].getReady()
                    self.teams[b].getReady()

                    # Manche 2
                    btl = Battle(self.teams[b].p + self.teams[a].p)
                    btl.processBattle()

                    if btl.winner >= 0:
                        self.teams[a].fitnessStep(1 - btl.winner, sum([self.teams[b].p[i].battleStats[0] for i in range(3)])/sum([self.teams[b].p[i].stats[0] for i in range(3)]), btl.turn)
                        self.teams[b].fitnessStep(1 - btl.winner, sum([self.teams[a].p[i].battleStats[0] for i in range(3)])/sum([self.teams[a].p[i].stats[0] for i in range(3)]), btl.turn)
