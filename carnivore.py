from agent import Agent
from herbivore import Herbivore
from herbivoreBody import HerbivoreBody
from superpredateur import Superpredateur
from superpredateurBody import SuperpredateurBody


class Carnivore(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.coefCreep = .01
        self.coefObs = 100

    def update(self):
        manqer, fuir = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length() * self.coefCreep)
            self.body.acceleration = self.body.acceleration + target

        if len(fuir) > 0:
            target = self.body.position - fuir[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * (self.coefObs + self.body.mass))
            self.body.acceleration += target

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
