import random

from pygame import Vector2

import core


class Vegetal(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = random.randint(2, 5)
        self.isAte = False
        self.becomesVegetal = False
        self.color = (216, 235, 91)

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)
