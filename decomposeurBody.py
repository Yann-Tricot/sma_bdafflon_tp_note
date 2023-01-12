from body import Body


class DecomposeurBody(Body):
    def __init__(self):
        super().__init__()

        self.faimMin = 0
        self.faimMax = 20

        self.fatigueMin = 0
        self.fatigueMax = 20

        self.reproductionMin = 0
        self.reproductionMax = 4

        self.esperanceVie = 20

        self.color = (145, 145, 145)
