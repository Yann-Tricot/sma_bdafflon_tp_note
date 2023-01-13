import time

from agent import Agent
from herbivoreBody import HerbivoreBody
from superpredateurBody import SuperpredateurBody


class Carnivore(Agent):
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

    def filtrePerception(self):
        manger = []
        fuir = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, HerbivoreBody) and i.isDead is False:
                manger.append(i)
            elif isinstance(i, SuperpredateurBody) and i.isDead is False:
                fuir.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)
        fuir.sort(key=lambda x: x.dist, reverse=False)

        return manger, fuir
