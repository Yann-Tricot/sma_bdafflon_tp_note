from body import Body


class SuperpredateurBody(Body):
    def __init__(self):
        super().__init__()

        self.faimMin = 0
        self.faimMax = 20

        self.fatigueMin = 0
        self.fatigueMax = 25

        self.reproductionMin = 0
        self.reproductionMax = 30

        self.esperanceVie = 40

        self.color = (252, 3, 3)
