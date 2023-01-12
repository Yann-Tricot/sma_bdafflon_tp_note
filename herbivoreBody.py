from body import Body


class HerbivoreBody(Body):
    def __init__(self):
        super().__init__()

        self.faimMin = 0
        self.faimMax = 5

        self.fatigueMin = 0
        self.fatigueMax = 7

        self.reproductionMin = 0
        self.reproductionMax = 12

        self.esperanceVie = 20

        self.color = (102, 212, 103)

