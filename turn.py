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
                result = []
                if a != b:

                    # # Manche 1
                    # b = Battle([self.teams[a].p[0], self.teams[a].p[1], self.teams[a].p[2],
                    #             self.teams[b].p[0], self.teams[b].p[1], self.teams[b].p[2]])
                    # b.processBattle()
                    # result.append(b.winner)
                    #
                    # # Manche 2
                    # b = Battle([self.teams[b].p[0], self.teams[a].p[b], self.teams[b].p[2],
                    #             self.teams[a].p[0], self.teams[a].p[1], self.teams[a].p[2]])
                    # b.processBattle()
                    # result.append(1 - b.winner)

                    # TODO: calcul du fitness
                    pass
