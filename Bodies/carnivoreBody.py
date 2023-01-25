import random

from Bodies.body import Body


class CarnivoreBody(Body):
    def __init__(self, g_vMax, g_accMax, g_mass, g_faimMax, g_fatigueMax, g_reproMax, g_vieMax):
        super().__init__()

        self.vMax = g_vMax
        self.accMax = g_accMax
        self.mass = g_mass

        self.faimMax = g_faimMax
        self.fatigueMax = g_fatigueMax
        self.reproductionMax = g_reproMax
        self.esperanceVie = g_vieMax

        self.color = (252, 111, 3)
