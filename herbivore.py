import time

from agent import Agent
from carnivoreBody import CarnivoreBody
from vegetal import Vegetal


class Herbivore(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.coefCreep = .01
        self.coefObs = 100

    def update(self):
        currentTime = time.time()
        manqer, fuir = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            self.body.acceleration = self.body.acceleration + target

        if len(fuir) > 0:
            target = self.body.position - fuir[0].position
            self.body.acceleration += target

        if (len(manqer) == 0 and len(fuir) == 0) and (currentTime - self.lastTickTime > 1):
            self.randomizeMove(currentTime)

    def eatOtherAgent(self, ateVegetal):
        if self.body.isDead is False and self.body.isSleeping is False:
            ateVegetal.isAte = True
            if self.body.faimMin > self.body.jaugeFaim - 5:
                self.body.jaugeFaim = self.body.faimMin
            else:
                self.body.jaugeFaim -= 5

    def filtrePerception(self):
        manger = []
        fuir = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Vegetal):
                manger.append(i)
                if self.otherAgentInKillZone(i) is True:
                    self.eatOtherAgent(i)
            elif isinstance(i, CarnivoreBody) and (i.isDead is False and i.isSleeping is False):
                fuir.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)
        fuir.sort(key=lambda x: x.dist, reverse=False)

        return manger, fuir
