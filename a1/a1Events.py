
class a1Event:

    actions = []

    def addListener(self, action):
        self.actions.append(action)

    def invoke(self):
        for action in self.actions:
            action()


        