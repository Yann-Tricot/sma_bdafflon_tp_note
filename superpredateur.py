import random

from pygame import Vector2

from agent import Agent
from carnivoreBody import CarnivoreBody


class Superpredateur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.coefCreep = .01

    def update(self):
        manqer = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            # target.scale_to_length(target.length() * self.coefCreep)
            self.body.acceleration += target
        else:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            self.body.acceleration += target

    def eatOtherAgent(self, ateAgent):
        ateAgent.isDead = True
        ateAgent.isAte = True
        if self.body.faimMin > self.body.jaugeFaim - 5:
            self.body.jaugeFaim = self.body.faimMin
        else:
            self.body.jaugeFaim -= 5

    def filtrePerception(self):
        manger = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, CarnivoreBody) and i.isDead is False:
                manger.append(i)
                if self.otherAgentInKillZone(i) is True:
                    self.eatOtherAgent(i)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger
