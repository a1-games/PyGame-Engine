
class a1Event:

    def __init__(self):
        self.actions = []

    def addListener(self, action):
        self.actions.append(action)

    def invoke(self, *args):
        if args:
            for action in self.actions:
                action(args)
        else:
            for action in self.actions:
                action()

    def isEmpty(self):
        if len(self.actions) == 0:
            return True
        return False

        