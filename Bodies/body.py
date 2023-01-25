import random
import time

from pygame import Vector2

import core
from fustrum import Fustrum


class Body(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.velocity = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.vMax = 2
        self.acceleration = Vector2()
        self.accMax = 10
        self.mass = 7
        self.fustrum = Fustrum(150, self)

        self.jaugeFaim = 0
        self.faimMin = 0
        self.faimMax = 0

        self.jaugeFatigue = 0
        self.fatigueMin = 0
        self.fatigueMax = 0
        self.startSleepStamp = 0
        self.sleepDuration = 3

        self.jaugeReproduction = 0
        self.reproductionMin = 0
        self.reproductionMax = 0
        self.isReadyToDuplicate = False

        self.dateNaissance = time.time()
        self.esperanceVie = 0

        self.isSleeping = False
        self.isDead = False
        self.isAte = False
        self.becomesVegetal = False

        self.color = (0, 0, 0)
        self.lastTickTime = 0

    def update(self):
        currentTime = time.time()

        if currentTime - self.dateNaissance > self.esperanceVie:
            self.isDead = True

        if currentTime - self.startSleepStamp > self.sleepDuration:
            self.isSleeping = False

        if self.isDead is False and self.isSleeping is False:
            if currentTime - self.lastTickTime > 1:
                self.jaugeFaim += 1
                self.jaugeFatigue += 1
                self.jaugeReproduction += 1
                self.lastTickTime = currentTime

            if self.jaugeFaim > self.faimMax:
                self.isDead = True

            if self.jaugeFatigue > self.fatigueMax and self.isDead is False:
                self.isSleeping = True
                self.jaugeFatigue = 0
                self.startSleepStamp = time.time()

            if self.jaugeReproduction > self.reproductionMax and self.isDead is False and self.isSleeping is False:
                self.isReadyToDuplicate = True

            self.move()

    def move(self):
        if self.acceleration.length() > self.accMax / self.mass:
            self.acceleration.scale_to_length(self.accMax / self.mass)

        self.velocity += self.acceleration

        if self.velocity.length() > self.vMax:
            self.velocity.scale_to_length(self.vMax)

        self.position += self.velocity
        core.Draw.line((255, 255, 255), self.position, self.position + self.acceleration * 100, 2)

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

    def reproduction(self):
        pass

    def show(self):
        # Draw body
        core.Draw.circle(self.color, self.position, self.mass)

        # Draw if Agent is dead or sleeping
        if self.isDead is True:
            core.Draw.text((255, 255, 255), 'Dead', Vector2(self.position.x + 5, self.position.y), 10, 'Arial')
        elif self.isSleeping is True:
            core.Draw.text((255, 255, 255), 'Sleep', Vector2(self.position.x + 5, self.position.y), 10, 'Arial')

        # Draw agent stats
        if self.isDead is False:
            core.Draw.text((255, 255, 255), 'faim: ' + str(self.jaugeFaim) + ' / ' + str(self.faimMax),
                           Vector2(self.position.x + 5, self.position.y + 8), 13, 'Arial')
            core.Draw.text((255, 255, 255), 'fatigue: ' + str(self.jaugeFatigue) + ' / ' + str(self.fatigueMax),
                           Vector2(self.position.x + 5, self.position.y + 20), 13, 'Arial')
            core.Draw.text((255, 255, 255),
                           'reprod.: ' + str(self.jaugeReproduction) + ' / ' + str(self.reproductionMax),
                           Vector2(self.position.x + 5, self.position.y + 32), 13, 'Arial')

        # TESTING PURPOSE
        # # #
        # Draw perception radius
        core.Draw.circle(self.color, self.position, self.fustrum.radius, 1)
        # Draw kill zone
        core.Draw.circle((255, 255, 255), self.position, self.mass, 1)
