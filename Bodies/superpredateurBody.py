import random

from pygame import Vector2

import core

from Agents.superpredateur import Superpredateur
from Bodies.body import Body


class SuperpredateurBody(Body):
    def __init__(self, g_vMax, g_accMax, g_mass, g_faimMax, g_fatigueMax, g_reproMax, g_vieMax):
        super().__init__()

        self.vMax = g_vMax
        self.accMax = g_accMax
        self.mass = g_mass

        self.faimMax = g_faimMax
        self.fatigueMax = g_fatigueMax
        self.reproductionMax = g_reproMax
        self.esperanceVie = g_vieMax

        self.color = (252, 3, 3)

    def reproduction(self):
        g_vMax = self.vMax + random.randint(0, 2) - random.randint(0, 2)
        if g_vMax <= 0:
            g_vMax = self.vMax

        g_accMax = self.accMax + random.randint(0, 2) - random.randint(0, 2)
        if g_accMax <= 0:
            g_accMax = self.accMax

        g_mass = self.mass + random.randint(0, 2) - random.randint(0, 2)
        if g_mass <= 0:
            g_mass = self.mass

        g_faimMax = self.faimMax + random.randint(0, 2) - random.randint(0, 2)
        if g_faimMax <= 0:
            g_faimMax = self.faimMax

        g_fatigueMax = self.fatigueMax + random.randint(0, 2) - random.randint(0, 2)
        if g_fatigueMax <= 0:
            g_fatigueMax = self.fatigueMax

        g_reproMax = self.reproductionMax + random.randint(0, 2) - random.randint(0, 2)
        if g_reproMax <= 0:
            g_reproMax = self.reproductionMax

        g_vieMax = self.esperanceVie + random.randint(0, 2) - random.randint(0, 2)
        if g_vieMax <= 0:
            g_vieMax = self.esperanceVie

        newBorn = Superpredateur(
            SuperpredateurBody(g_vMax, g_accMax, g_mass, g_faimMax, g_fatigueMax, g_reproMax, g_vieMax))
        newBorn.body.position = self.position + Vector2(random.randint(-1, 1), random.randint(-1, 1))

        core.memory('superpredateurs').append(newBorn)
        self.jaugeReproduction = self.reproductionMin
        self.isReadyToDuplicate = False
