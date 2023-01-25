import json
import random
import threading
import time

import pygame
from matplotlib import pyplot as plt
from pygame import Vector2

import core
from Agents.carnivore import Carnivore
from Agents.decomposeur import Decomposeur
from Agents.herbivore import Herbivore
from Agents.superpredateur import Superpredateur
from Bodies.carnivoreBody import CarnivoreBody
from Bodies.decomposeurBody import DecomposeurBody
from Bodies.herbivoreBody import HerbivoreBody
from Bodies.superpredateurBody import SuperpredateurBody
from vegetal import Vegetal


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1280, 1024]

    # # #
    # Load 'scenario.json' file and extract data
    scenarioConfigFile = open('scenario.json')
    scenarioConfigData = json.load(scenarioConfigFile)
    scenarioConfigFile.close()

    core.memory("dureeSimu", scenarioConfigData['dureeSimu'])
    core.memory("timer", time.time())
    core.memory("lastTickTime", 0)

    suppredasData = scenarioConfigData['SuperPredateur']
    carnisData = scenarioConfigData['Carnivores']
    herbisData = scenarioConfigData['Herbivore']
    decomposData = scenarioConfigData['Decomposeur']
    vegetalsData = scenarioConfigData['Vegetal']

    core.memory("superpredateurs", [])
    core.memory("nbSuperpredateurs", suppredasData['nb'])

    core.memory("carnivores", [])
    core.memory("nbCarnivores", carnisData['nb'])

    core.memory("herbivores", [])
    core.memory("nbHerbivores", herbisData['nb'])

    core.memory("decomposeurs", [])
    core.memory("nbDecomposeurs", decomposData['nb'])

    core.memory("vegetals", [])
    core.memory("nbVegetals", vegetalsData['nb'])

    # # #
    # Species initialization according 'scenario.json' file content (randomize stats)
    for i in range(0, core.memory("nbSuperpredateurs")):
        core.memory("superpredateurs").append(Superpredateur(SuperpredateurBody(
            random.randint(suppredasData['parametres']['vitesseMax'][0], suppredasData['parametres']['vitesseMax'][1]),
            random.randint(suppredasData['parametres']['accelerationMax'][0],
                           suppredasData['parametres']['accelerationMax'][1]),
            random.randint(suppredasData['parametres']['massMax'][0], suppredasData['parametres']['massMax'][1]),
            random.randint(suppredasData['parametres']['MaxFaim'][0], suppredasData['parametres']['MaxFaim'][1]),
            random.randint(suppredasData['parametres']['MaxFatigue'][0], suppredasData['parametres']['MaxFatigue'][1]),
            random.randint(suppredasData['parametres']['MaxReproduction'][0],
                           suppredasData['parametres']['MaxReproduction'][1]),
            random.randint(suppredasData['parametres']['MaxVie'][0], suppredasData['parametres']['MaxVie'][1])
        )))

    for i in range(0, core.memory("nbCarnivores")):
        core.memory("carnivores").append(Carnivore(CarnivoreBody(
            random.randint(carnisData['parametres']['vitesseMax'][0], carnisData['parametres']['vitesseMax'][1]),
            random.randint(carnisData['parametres']['accelerationMax'][0],
                           carnisData['parametres']['accelerationMax'][1]),
            random.randint(carnisData['parametres']['massMax'][0], carnisData['parametres']['massMax'][1]),
            random.randint(carnisData['parametres']['MaxFaim'][0], carnisData['parametres']['MaxFaim'][1]),
            random.randint(carnisData['parametres']['MaxFatigue'][0], carnisData['parametres']['MaxFatigue'][1]),
            random.randint(carnisData['parametres']['MaxReproduction'][0],
                           carnisData['parametres']['MaxReproduction'][1]),
            random.randint(carnisData['parametres']['MaxVie'][0], carnisData['parametres']['MaxVie'][1])
        )))

    for i in range(0, core.memory("nbHerbivores")):
        core.memory("herbivores").append(Herbivore(HerbivoreBody(
            random.randint(herbisData['parametres']['vitesseMax'][0], herbisData['parametres']['vitesseMax'][1]),
            random.randint(herbisData['parametres']['accelerationMax'][0],
                           herbisData['parametres']['accelerationMax'][1]),
            random.randint(herbisData['parametres']['massMax'][0], herbisData['parametres']['massMax'][1]),
            random.randint(herbisData['parametres']['MaxFaim'][0], herbisData['parametres']['MaxFaim'][1]),
            random.randint(herbisData['parametres']['MaxFatigue'][0], herbisData['parametres']['MaxFatigue'][1]),
            random.randint(herbisData['parametres']['MaxReproduction'][0],
                           herbisData['parametres']['MaxReproduction'][1]),
            random.randint(herbisData['parametres']['MaxVie'][0], herbisData['parametres']['MaxVie'][1])
        )))

    for i in range(0, core.memory("nbDecomposeurs")):
        core.memory("decomposeurs").append(Decomposeur(DecomposeurBody(
            random.randint(decomposData['parametres']['vitesseMax'][0], decomposData['parametres']['vitesseMax'][1]),
            random.randint(decomposData['parametres']['accelerationMax'][0],
                           decomposData['parametres']['accelerationMax'][1]),
            random.randint(decomposData['parametres']['massMax'][0], decomposData['parametres']['massMax'][1]),
            random.randint(decomposData['parametres']['MaxFaim'][0], decomposData['parametres']['MaxFaim'][1]),
            random.randint(decomposData['parametres']['MaxFatigue'][0], decomposData['parametres']['MaxFatigue'][1]),
            random.randint(decomposData['parametres']['MaxReproduction'][0],
                           decomposData['parametres']['MaxReproduction'][1]),
            random.randint(decomposData['parametres']['MaxVie'][0], decomposData['parametres']['MaxVie'][1])
        )))

    for i in range(0, core.memory("nbVegetals")):
        core.memory("vegetals").append(Vegetal(random.randint(vegetalsData['parametres']['massMax'][0],
                                                              vegetalsData['parametres']['massMax'][1])))

    plotThread = threading.Thread(target=draw_graph, args=())
    plotThread.start()
    print("Setup END-----------")


def computePerception(agent, predas, carnis, herbis, decompos, vegetals):
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

    for b in vegetals:
        if agent.body.fustrum.inside(b):
            agent.body.fustrum.perceptionList.append(b)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()


def updateEnv(superPredas, carnis, herbis, decompos, vegetals):
    for superPreda in superPredas:
        if superPreda.body.isDead is True:
            if superPreda.body.isAte is True:
                if superPreda.body.becomesVegetal is True:
                    newVegetal = Vegetal(random.randint(2, 5))
                    core.memory("vegetals").append(newVegetal)
                core.memory("superpredateurs").remove(superPreda)
        else:
            # BIRTHS CHECK
            if superPreda.body.isReadyToDuplicate is True:
                superPreda.body.reproduction()

    for carni in carnis:
        if carni.body.isDead is True:
            if carni.body.isAte is True:
                if carni.body.becomesVegetal is True:
                    newVegetal = Vegetal(random.randint(2, 5))
                    core.memory("vegetals").append(Vegetal(random.randint(2, 5)))
                core.memory("carnivores").remove(carni)
        else:
            # BIRTHS CHECK
            if carni.body.isReadyToDuplicate is True:
                g_vMax = carni.body.vMax + random.randint(0, 2) - random.randint(0, 2)
                if g_vMax <= 0:
                    g_vMax = carni.body.vMax

                g_accMax = carni.body.accMax + random.randint(0, 2) - random.randint(0, 2)
                if g_accMax <= 0:
                    g_accMax = carni.body.accMax

                g_mass = carni.body.mass + random.randint(0, 2) - random.randint(0, 2)
                if g_mass <= 0:
                    g_mass = carni.body.mass

                g_faimMax = carni.body.faimMax + random.randint(0, 2) - random.randint(0, 2)
                if g_faimMax <= 0:
                    g_faimMax = carni.body.faimMax

                g_fatigueMax = carni.body.fatigueMax + random.randint(0, 2) - random.randint(0, 2)
                if g_fatigueMax <= 0:
                    g_fatigueMax = carni.body.fatigueMax

                g_reproMax = carni.body.reproductionMax + random.randint(0, 2) - random.randint(0, 2)
                if g_reproMax <= 0:
                    g_reproMax = carni.body.reproductionMax

                g_vieMax = carni.body.esperanceVie + random.randint(0, 2) - random.randint(0, 2)
                if g_vieMax <= 0:
                    g_vieMax = carni.body.esperanceVie

                newBorn = Carnivore(
                    CarnivoreBody(g_vMax, g_accMax, g_mass, g_faimMax, g_fatigueMax, g_reproMax, g_vieMax))
                newBorn.body.position = carni.body.position + Vector2(random.randint(-1, 1), random.randint(-1, 1))

                core.memory('carnivores').append(newBorn)
                carni.body.jaugeReproduction = carni.body.reproductionMin
                carni.body.isReadyToDuplicate = False

    for herbi in herbis:
        if herbi.body.isDead is True:
            if herbi.body.isAte is True:
                if herbi.body.becomesVegetal is True:
                    newVegetal = Vegetal(random.randint(2, 5))
                    core.memory("vegetals").append(newVegetal)
                core.memory("herbivores").remove(herbi)
        else:
            # BIRTHS CHECK
            if herbi.body.isReadyToDuplicate is True:
                g_vMax = herbi.body.vMax + random.randint(0, 2) - random.randint(0, 2)
                if g_vMax <= 0:
                    g_vMax = herbi.body.vMax

                g_accMax = herbi.body.accMax + random.randint(0, 2) - random.randint(0, 2)
                if g_accMax <= 0:
                    g_accMax = herbi.body.accMax

                g_mass = herbi.body.mass + random.randint(0, 2) - random.randint(0, 2)
                if g_mass <= 0:
                    g_mass = herbi.body.mass

                g_faimMax = herbi.body.faimMax + random.randint(0, 2) - random.randint(0, 2)
                if g_faimMax <= 0:
                    g_faimMax = herbi.body.faimMax

                g_fatigueMax = herbi.body.fatigueMax + random.randint(0, 2) - random.randint(0, 2)
                if g_fatigueMax <= 0:
                    g_fatigueMax = herbi.body.fatigueMax

                g_reproMax = herbi.body.reproductionMax + random.randint(0, 2) - random.randint(0, 2)
                if g_reproMax <= 0:
                    g_reproMax = herbi.body.reproductionMax

                g_vieMax = herbi.body.esperanceVie + random.randint(0, 2) - random.randint(0, 2)
                if g_vieMax <= 0:
                    g_vieMax = herbi.body.esperanceVie

                newBorn = Herbivore(
                    HerbivoreBody(g_vMax, g_accMax, g_mass, g_faimMax, g_fatigueMax, g_reproMax, g_vieMax))
                newBorn.body.position = herbi.body.position + Vector2(random.randint(-1, 1), random.randint(-1, 1))

                core.memory('herbivores').append(newBorn)
                herbi.body.jaugeReproduction = herbi.body.reproductionMin
                herbi.body.isReadyToDuplicate = False

    for decompo in decompos:
        if decompo.body.isDead is True:
            if decompo.body.isAte is True:
                core.memory("decomposeurs").remove(decompo)
        else:
            # BIRTHS CHECK
            if decompo.body.isReadyToDuplicate is True:
                decompo.body.reproduction()

    for vegetal in vegetals:
        if vegetal.isAte is True:
            core.memory("vegetals").remove(vegetal)


def getCurrentStats(superPredas, carnis, herbis, decompos):
    if len(superPredas) > 0:
        bestSuperpreda = superPredas[0]
    else:
        bestSuperpreda = None
    percSuperpredas = 0
    totSuperpredas = 0

    if len(carnis) > 0:
        bestCarni = carnis[0]
    else:
        bestCarni = None
    percCarnis = 0
    totCarnis = 0

    if len(herbis) > 0:
        bestHerbi = herbis[0]
    else:
        bestHerbi = None
    percHerbis = 0
    totHerbis = 0

    if len(decompos) > 0:
        bestDecompo = decompos[0]
    else:
        bestDecompo = None
    percDecompos = 0
    totDecompos = 0

    for superPreda in superPredas:
        percSuperpredas += 1
        if superPreda.body.isDead is False:
            totSuperpredas += 1
            if superPreda.body.vMax >= bestSuperpreda.body.vMax and \
                    superPreda.body.faimMax >= bestSuperpreda.body.faimMax and \
                    superPreda.body.fatigueMax >= bestSuperpreda.body.fatigueMax and \
                    superPreda.body.mass >= bestSuperpreda.body.mass and \
                    superPreda.body.esperanceVie >= bestSuperpreda.body.esperanceVie:
                bestSuperpreda = superPreda

    for carni in carnis:
        percCarnis += 1
        if carni.body.isDead is False:
            totCarnis += 1
            if carni.body.vMax >= bestCarni.body.vMax and \
                    carni.body.faimMax >= bestCarni.body.faimMax and \
                    carni.body.fatigueMax >= bestCarni.body.fatigueMax and \
                    carni.body.mass >= bestCarni.body.mass and \
                    carni.body.esperanceVie >= bestCarni.body.esperanceVie:
                bestCarni = carni

    for herbi in herbis:
        percHerbis += 1
        if herbi.body.isDead is False:
            totHerbis += 1
            if herbi.body.vMax >= bestHerbi.body.vMax and \
                    herbi.body.faimMax >= bestHerbi.body.faimMax and \
                    herbi.body.fatigueMax >= bestHerbi.body.fatigueMax and \
                    herbi.body.mass >= bestHerbi.body.mass and \
                    herbi.body.esperanceVie >= bestHerbi.body.esperanceVie:
                bestHerbi = herbi

    for decompo in decompos:
        percDecompos += 1
        if decompo.body.isDead is False:
            totDecompos += 1
            if decompo.body.vMax >= bestDecompo.body.vMax and \
                    decompo.body.faimMax >= bestDecompo.body.faimMax and \
                    decompo.body.fatigueMax >= bestDecompo.body.fatigueMax and \
                    decompo.body.mass >= bestDecompo.body.mass and \
                    decompo.body.esperanceVie >= bestDecompo.body.esperanceVie:
                bestDecompo = decompo

    dataStats = {'SUPER_PREDATEUR': totSuperpredas,
                 'CARNIVORE': totCarnis,
                 'HERBIVORE': totHerbis,
                 'DECOMPOSITEUR': totDecompos
                 }

    totAgents = percSuperpredas + percCarnis + percHerbis + percDecompos
    percSuperpredas = (percSuperpredas * 100) / totAgents
    percCarnis = (percCarnis * 100) / totAgents
    percHerbis = (percHerbis * 100) / totAgents
    percDecompos = (percDecompos * 100) / totAgents

    return dataStats, totAgents, bestSuperpreda, percSuperpredas, bestCarni, percCarnis, bestHerbi, percHerbis, \
        bestDecompo, percDecompos


def showStatsLog(superPredas, carnis, herbis, decompos):
    dataStats, totAgents, bestSuperpreda, percSuperpredas, bestCarni, percCarnis, bestHerbi, percHerbis, bestDecompo, \
        percDecompos = getCurrentStats(superPredas, carnis, herbis, decompos)

    print('SIMULATION STATISTICS')
    print('- - - - - - - - - - -')
    print('| tot. pop. : ' + str(totAgents) + 'agents')
    print('| superpredateurs : ', "%.2f" % percSuperpredas + '%')
    print('| carnivores : ', "%.2f" % percCarnis + '%')
    print('| herbivores : ', "%.2f" % percHerbis + '%')
    print('| decomposeurs : ', "%.2f" % percDecompos + '%')
    print('- - - - - - - - - - -')

    if bestSuperpreda is not None:
        print('| Best superpredateur : ', str(bestSuperpreda.uuid))
        print('| Stats --> : ',
              'vMax: ' + str(bestSuperpreda.body.vMax) + ' | ',
              'faimMax: ' + str(bestSuperpreda.body.faimMax) + ' | ',
              'fatigueMax: ' + str(bestSuperpreda.body.fatigueMax) + ' | ',
              'mass: ' + str(bestSuperpreda.body.mass) + ' | ',
              'esperanceVie: ' + str(bestSuperpreda.body.esperanceVie))
        print('|')

    if bestCarni is not None:
        print('| Best carnivore : ', str(bestCarni.uuid))
        print('| Stats --> : ',
              'vMax: ' + str(bestCarni.body.vMax) + ' | ',
              'faimMax: ' + str(bestCarni.body.faimMax) + ' | ',
              'fatigueMax: ' + str(bestCarni.body.fatigueMax) + ' | ',
              'mass: ' + str(bestCarni.body.mass) + ' | ',
              'esperanceVie: ' + str(bestCarni.body.esperanceVie))
        print('|')

    if bestHerbi is not None:
        print('| Best herbivore : ', str(bestHerbi.uuid))
        print('| Stats --> : ',
              'vMax: ' + str(bestHerbi.body.vMax) + ' | ',
              'faimMax: ' + str(bestHerbi.body.faimMax) + ' | ',
              'fatigueMax: ' + str(bestHerbi.body.fatigueMax) + ' | ',
              'mass: ' + str(bestHerbi.body.mass) + ' | ',
              'esperanceVie: ' + str(bestHerbi.body.esperanceVie))
        print('|')

    if bestDecompo is not None:
        print('| Best decomposeur : ', str(bestDecompo.uuid))
        print('| Stats --> : ',
              'vMax: ' + str(bestDecompo.body.vMax) + ' | ',
              'faimMax: ' + str(bestDecompo.body.faimMax) + ' | ',
              'fatigueMax: ' + str(bestDecompo.body.fatigueMax) + ' | ',
              'mass: ' + str(bestDecompo.body.mass) + ' | ',
              'esperanceVie: ' + str(bestDecompo.body.esperanceVie))
        print('|')
    print('- - - - - - - - - - -')


history_time = []
history_data = {"SUPER_PREDATEUR": [], "CARNIVORE": [], "HERBIVORE": [], "DECOMPOSITEUR": []}


def draw_graph():
    while True:
        global history_data
        global history_time

        dataStats, totAgents, bestSuperpreda, percSuperpredas, bestCarni, percCarnis, bestHerbi, percHerbis, \
            bestDecompo, percDecompos = getCurrentStats(core.memory("superpredateurs"), core.memory("carnivores"),
                                                        core.memory("herbivores"), core.memory("decomposeurs"))

        plt.cla()
        current_time = pygame.time.get_ticks() / 1000
        history_time.append(current_time)
        for key in history_data.keys():
            history_data[key].append(dataStats[key])
            if key == "SUPER_PREDATEUR":
                plt.plot(history_time, history_data[key], 'red', label=key)
            elif key == "CARNIVORE":
                plt.plot(history_time, history_data[key], 'orange', label=key)
            elif key == "HERBIVORE":
                plt.plot(history_time, history_data[key], 'green', label=key)
            elif key == "DECOMPOSITEUR":
                plt.plot(history_time, history_data[key], 'gray', label=key)

        plt.xlabel('Time (sec.)')
        plt.ylabel('Nb. specimens')
        plt.legend(loc="lower left")
        plt.title("Evolution amount of specimen by time")
        plt.draw()
        plt.show()
        plt.pause(0.001)


def stopExecution():
    if time.time() - core.memory("lastTickTime") > 1:
        print('Session duration: ' + str(int(time.time() - core.memory("timer"))) + '/' + str(core.memory('dureeSimu')))
        core.memory("lastTickTime", time.time())
    if time.time() - core.memory("timer") > float(core.memory('dureeSimu')):
        exit()


def run():
    core.cleanScreen()

    if core.getKeyPressList("s"):
        showStatsLog(core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                     core.memory("decomposeurs"))

    if core.getKeyPressList("ESCAPE"):
        pygame.quit()

    # Display
    for agent in core.memory("superpredateurs"):
        agent.body.show()

    for agent in core.memory("carnivores"):
        agent.body.show()

    for agent in core.memory("decomposeurs"):
        agent.body.show()

    for agent in core.memory("herbivores"):
        agent.body.show()

    for vegetal in core.memory("vegetals"):
        vegetal.show()

    # Actions
    # computePerception ALL
    for agent in core.memory("superpredateurs"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"), core.memory("vegetals"))

    for agent in core.memory("carnivores"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"), core.memory("vegetals"))

    for agent in core.memory("decomposeurs"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"), core.memory("vegetals"))

    for agent in core.memory("herbivores"):
        computePerception(agent, core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
                          core.memory("decomposeurs"), core.memory("vegetals"))

    # computeDecision ALL
    for agent in core.memory("superpredateurs"):
        computeDecision(agent)

    for agent in core.memory("carnivores"):
        computeDecision(agent)

    for agent in core.memory("decomposeurs"):
        computeDecision(agent)

    for agent in core.memory("herbivores"):
        computeDecision(agent)

    # applyDecision ALL
    for agent in core.memory("superpredateurs"):
        applyDecision(agent)

    for agent in core.memory("carnivores"):
        applyDecision(agent)

    for agent in core.memory("decomposeurs"):
        applyDecision(agent)

    for agent in core.memory("herbivores"):
        applyDecision(agent)

    stopExecution()
    updateEnv(core.memory("superpredateurs"), core.memory("carnivores"), core.memory("herbivores"),
              core.memory("decomposeurs"), core.memory("vegetals"))


core.main(setup, run)
