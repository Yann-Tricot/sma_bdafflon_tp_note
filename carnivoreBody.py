from body import Body


class CarnivoreBody(Body):
    def __init__(self):
        super().__init__()

        self.faimMin = 0
        self.faimMax = 13

        self.fatigueMin = 0
        self.fatigueMax = 7

        self.reproductionMin = 0
        self.reproductionMax = 15

        self.esperanceVie = 35

        self.color = (252, 111, 3)
