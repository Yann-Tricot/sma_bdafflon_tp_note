import core


class Vegetal(object):
    def __init__(self):
        pass

    def show(self):
        core.Draw.circle(self.color[self.status], self.body.position, self.body.mass)