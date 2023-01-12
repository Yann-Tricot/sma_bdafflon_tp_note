import uuid

import core


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = uuid.uuid4()

    def show(self):
        core.Draw.circle(self.body.color, self.body.position, self.body.mass)