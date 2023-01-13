from body import Body


class SuperpredateurBody(Body):
    def __init__(self):
        super().__init__()

        self.faimMin = 0
        self.faimMax = 15

        self.fatigueMin = 0
        self.fatigueMax = 5

        self.reproductionMin = 0
        self.reproductionMax = 20

        self.esperanceVie = 30

        self.color = (252, 3, 3)
