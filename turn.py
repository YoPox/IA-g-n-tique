import numpy as np
from util import *
from battle import *
import math
import random


class Turnament:
    # Constructor

    def __init__(self, indices):
        self.indices = indices

    def process(self):

        # COMBATS EN N(N-1)

        for a in range(indices):
            for b in range(indices):
                result = []
                if a != b:
                    # Manche 1
                    b = Battle([teams[indices[a]].p[0], teams[indices[a]].p[1], teams[indices[a]].p[2],
                                teams[indices[b]].p[0], teams[indices[b]].p[1], teams[indices[b]].p[2]])
                    b.processBattle()
                    result.append(b.winner)

                    # Manche 2
                    b = Battle([teams[indices[b]].p[0], teams[indices[b]].p[1], teams[indices[b]].p[2],
                                teams[indices[a]].p[0], teams[indices[a]].p[1], teams[indices[a]].p[2]])
                    b.processBattle()
                    result.append(b.winner)

                    # TODO: calcul du fitness
