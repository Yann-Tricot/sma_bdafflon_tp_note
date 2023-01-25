import time

from Agents.agent import Agent
from Bodies.carnivoreBody import CarnivoreBody


class Superpredateur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.coefCreep = .01

    def update(self):
        currentTime = time.time()
        manqer = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            self.body.acceleration += target
        elif currentTime - self.lastTickTime > 1:
            self.randomizeMove(currentTime)

    def eatOtherAgent(self, ateAgent):
        if self.body.isDead is False and self.body.isSleeping is False:
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
