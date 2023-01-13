import random

import core
from carnivore import Carnivore
from decomposeur import Decomposeur
from herbivore import Herbivore
from superpredateur import Superpredateur
from carnivoreBody import CarnivoreBody
from decomposeurBody import DecomposeurBody
from herbivoreBody import HerbivoreBody
from superpredateurBody import SuperpredateurBody


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1200, 780]
    # core.fullscreen = True

    core.memory("superpredateurs", [])
    core.memory("nbSuperpredateurs", 5)

    core.memory("carnivores", [])
    core.memory("nbCarnivores", 20)

    core.memory("herbivores", [])
    core.memory("nbHerbivores", 0)

    core.memory("decomposeurs", [])
    core.memory("nbDecomposeurs", 0)

    core.memory("item", [])

    for i in range(0, core.memory("nbSuperpredateurs")):
        core.memory("superpredateurs").append(Superpredateur(SuperpredateurBody()))

    for i in range(0, core.memory("nbCarnivores")):
        core.memory("carnivores").append(Carnivore(CarnivoreBody()))

    for i in range(0, core.memory("nbDecomposeurs")):
        core.memory("decomposeurs").append(Decomposeur(DecomposeurBody()))

    for i in range(0, core.memory("nbHerbivores")):
        core.memory("herbivores").append(Herbivore(HerbivoreBody()))

    print("Setup END-----------")


def computePerception(agent, predas, carnis, herbis, decompos):
    agent.body.fustrum.perceptionList = []
    for b in predas:
        if agent.uuid != b.uuid:
            if agent.body.fustrum.inside(b.body):
                agent.body.fustrum.perceptionList.append(b.body)

    for b in carnis:
        if agent.uuid != b.uuid:
            if agent.body.fustrum.inside(b.body):
                agent.body.fustrum.perceptionList.append(b.body)

    for b in herbis:
        if agent.uuid != b.uuid:
            if agent.body.fustrum.inside(b.body):
                agent.body.fustrum.perceptionList.append(b.body)

    for b in decompos:
        if agent.uuid != b.uuid:
            if agent.body.fustrum.inside(b.body):
                agent.body.fustrum.perceptionList.append(b.body)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()


def checkNaissances(superPredas, carnis, herbis, decompos):
    for superPreda in superPredas:
        if superPreda.body.isReadyToDuplicate is True:
            newBorn = Superpredateur(SuperpredateurBody())
            # newBorn.body.position = superPreda.body.position
            # newBorn.body.vMax = random.randint(3, 6)
            # newBorn.body.mass = random.randint(6, 9)
            newBorn.body.faimMax = random.randint(20, 30)
            newBorn.body.fatigueMax = random.randint(25, 35)
            newBorn.body.reproductionMax = random.randint(40, 50)

            core.memory("superpredateurs").append(newBorn)
            superPreda.body.isReadyToDuplicate = False
            superPreda.body.jaugeReproduction = 0

    for carni in carnis:
        if carni.body.isReadyToDuplicate is True:
            newBorn = Carnivore(CarnivoreBody())
            # newBorn.body.position = carni.body.position
            # newBorn.body.vMax = random.randint(3, 5)
            # newBorn.body.mass = random.randint(6, 8)
            newBorn.body.faimMax = random.randint(15, 25)
            newBorn.body.fatigueMax = random.randint(20, 30)
            newBorn.body.reproductionMax = random.randint(35, 45)

            core.memory("carnivores").append(newBorn)
            carni.body.isReadyToDuplicate = False
            carni.body.jaugeReproduction = 0

    for herbi in herbis:
        if herbi.body.isReadyToDuplicate is True:
            newBorn = Herbivore(HerbivoreBody())
            # newBorn.body.position = herbi.body.position
            # newBorn.body.vMax = random.randint(3, 6)
            # newBorn.body.mass = random.randint(5, 7)
            newBorn.body.faimMax = random.randint(5, 10)
            newBorn.body.fatigueMax = random.randint(10, 15)
            newBorn.body.reproductionMax = random.randint(5, 10)

            core.memory("herbivores").append(newBorn)
            herbi.body.isReadyToDuplicate = False
            herbi.body.jaugeReproduction = 0

    for decompo in decompos:
        if decompo.body.isReadyToDuplicate is True:
            newBorn = Decomposeur(DecomposeurBody())
            newBorn.body.position = decompo.body.position
            # newBorn.body.vMax = random.randint(4, 6)
            # newBorn.body.mass = random.randint(3, 5)
            newBorn.body.faimMax = random.randint(8, 10)
            newBorn.body.fatigueMax = random.randint(10, 15)
            newBorn.body.reproductionMax = random.randint(2, 4)

            core.memory("decomposeurs").append(newBorn)
            decompo.body.isReadyToDuplicate = False
            decompo.body.jaugeReproduction = 0


def updateEnv(superPredas, carnis, herbis, decompos):
    for superPreda in superPredas:
        if superPreda.body.isDead is True:
            if superPreda.body.isAte is True:
                core.memory("superpredateurs").remove(superPreda)
        else:
            # BIRTHS CHECK
            if superPreda.body.isReadyToDuplicate is True:
                pass

    for carni in carnis:
        if carni.body.isDead is True:
            if carni.body.isAte is True:
                core.memory("carnivores").remove(carni)
        else:
            # BIRTHS CHECK
            if carni.body.isReadyToDuplicate is True:
                pass


    for herbi in herbis:
        if herbi.body.isDead is True:
            if herbi.body.isAte is True:
                core.memory("herbivores").remove(herbi)
        else:
            # BIRTHS CHECK
            if herbi.body.isReadyToDuplicate is True:
                pass


    for decompo in decompos:
        if decompo.body.isDead is True:
            if decompo.body.isAte is True:
                core.memory("decomposeurs").remove(decompo)
        else:
            # BIRTHS CHECK
            if decompo.body.isReadyToDuplicate is True:
                pass


def getCurrentStats(agents):
    pass


def showStatsLog(agents):
    pass


def run():
    core.cleanScreen()

    if core.getKeyPressList("s"):
        showStatsLog(core.memory("agents"))

    # Display
    for agent in core.memory("superpredateurs"):
        agent.body.show()

    for agent in core.memory("carnivores"):
        agent.body.show()

    for agent in core.memory("decomposeurs"):
        agent.body.show()

    for agent in core.memory("herbivores"):
        agent.body.show()

    for item in core.memory("item"):
        agent.body.show()

    # Actions
    # superpredateurs
    for agent in core.memory("superpredateurs"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"))

    for agent in core.memory("superpredateurs"):
        computeDecision(agent)

    for agent in core.memory("superpredateurs"):
        applyDecision(agent)

    # carnivores
    for agent in core.memory("carnivores"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"))

    for agent in core.memory("carnivores"):
        computeDecision(agent)

    for agent in core.memory("carnivores"):
        applyDecision(agent)

    # decomposeurs
    for agent in core.memory("decomposeurs"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"))

    for agent in core.memory("decomposeurs"):
        computeDecision(agent)

    for agent in core.memory("decomposeurs"):
        applyDecision(agent)

    # herbivores
    for agent in core.memory("herbivores"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"))

    for agent in core.memory("herbivores"):
        computeDecision(agent)

    for agent in core.memory("herbivores"):
        applyDecision(agent)

    updateEnv(core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                    core.memory("decomposeurs"))

core.main(setup, run)
