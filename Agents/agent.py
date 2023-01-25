import random
import uuid

from pygame import Vector2

import core


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = uuid.uuid4()
        self.lastTickTime = 0

    def randomizeMove(self, currentTime):
        self.lastTickTime = currentTime
        target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        while target.length() == 0:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        self.body.acceleration += target

    def otherAgentInKillZone(self, otherAgent):
        if otherAgent.position.distance_to(self.body.position) < self.body.mass + otherAgent.mass:
            return True
        else:
            False

    def show(self):
        core.Draw.circle(self.body.color, self.body.position, self.body.mass)
