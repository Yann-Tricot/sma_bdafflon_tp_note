import core


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [900, 600]

    core.memory("agents", [])
    core.memory("nbAgents", 200)
    core.memory("item", [])

    # for i in range(0, core.memory("nbAgents")):
    #     core.memory("agents").append(Agent(Body()))

    print("Setup END-----------")


def computePerception(agent):
    pass


def computeDecision(agent):
    pass


def applyDecision(agent):
    pass


def run():
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("item"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)


core.main(setup, run)
