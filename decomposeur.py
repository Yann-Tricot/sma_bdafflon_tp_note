from agent import Agent
from carnivoreBody import CarnivoreBody
from herbivoreBody import HerbivoreBody
from superpredateurBody import SuperpredateurBody


class Decomposeur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.coefCreep = .01
        self.coefObs = 100

    def update(self):
        manqer = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length() * self.coefCreep)
            self.body.acceleration = self.body.acceleration + target

    def filtrePerception(self):
        manger = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, HerbivoreBody) and i.isDead is True:
                manger.append(i)
            elif isinstance(i, SuperpredateurBody) and i.isDead is True:
                manger.append(i)
            elif isinstance(i, CarnivoreBody) and i.isDead is True:
                manger.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger