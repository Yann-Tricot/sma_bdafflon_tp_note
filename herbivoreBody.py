from body import Body


class HerbivoreBody(Body):
    def __init__(self):
        super().__init__()

        self.faimMin = 0
        self.faimMax = 10

        self.fatigueMin = 0
        self.fatigueMax = 12

        self.reproductionMin = 0
        self.reproductionMax = 10

        self.esperanceVie = 35

        self.color = (102, 212, 103)

