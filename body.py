import random
import time

from pygame import Vector2

import core
from fustrum import Fustrum


class Body(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.velocity = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.vMax = 4
        self.acceleration = Vector2()
        self.accMax = 1
        self.mass = 7
        self.fustrum = Fustrum(150, self)

        self.jaugeFaim = 0
        self.faimMin = 0
        self.faimMax = 0

        self.jaugeFatigue = 0
        self.fatigueMin = 0
        self.fatigueMax = 0

        self.jaugeReproduction = 0
        self.reproductionMin = 0
        self.reproductionMax = 0
        self.isReadyToDuplicate = False

        self.dateNaissance = time.time()
        self.esperanceVie = 0

        self.isSleeping = False
        self.isDead = False

        self.color = (0, 0, 0)
        self.lastTickTime = 0

    def update(self):
        currentTime = time.time()
        if currentTime - self.lastTickTime > 1:
            self.jaugeFaim += 1
            self.jaugeFatigue += 1
            self.jaugeReproduction += 1
            self.lastTickTime = currentTime

        if currentTime - self.dateNaissance > self.esperanceVie:
            self.isDead = True

        if self.isSleeping is False and self.isDead is False:
            if self.jaugeFaim > self.faimMax:
                self.isDead = True

            if self.jaugeFatigue > self.fatigueMax and self.isDead is False:
                self.isSleeping

            if self.jaugeReproduction > self.reproductionMax and self.isDead is False and self.isSleeping is False:
                self.isReadyToDuplicate = True
                self.jaugeReproduction = 0

            self.move()

    def move(self):
        if self.acceleration.length() > self.accMax / self.mass:
            self.acceleration.scale_to_length(self.accMax / self.mass)

        self.velocity += self.acceleration

        if self.velocity.length() > self.vMax:
            self.velocity.scale_to_length(self.vMax)

        self.position += self.velocity

        self.acceleration = Vector2()
        self.edge()

    def edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)
        core.Draw.circle(self.color, self.position, self.fustrum.radius, 1)