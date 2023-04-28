import abc
import time

class Scene(metaclass=abc.ABCMeta):

    _initiated = False
    _active = True

    def disable(self):
        self._active = False


    def setOpacity(self, opacity):
        if self._initiated == False:
            print("ERROR: Setting scene opacity before scene was initiated!")
            return
        self.opacity = opacity
        for gameobject in self.gameobjects:
            gameobject.setOpacity(opacity)

    def addGameObject(self, gameobject):
        self.gameobjects.append(gameobject)

    def destroyGameObject(self, gameobject):
        self.gameobjects.remove(gameobject)

    def draw(self, screen):
        #print("is drawing")
        for gameobject in self.gameobjects:
            #print("is drawing a spriterect in spriterects")
            gameobject.draw(screen, self)

    def update(self):
        #print("is drawing")
        for gameobject in self.gameobjects:
            #print("is drawing a spriterect in spriterects")
            gameobject.update()
            
    def handleEvents(self, events):
        # handle events
        pass
    

    def InitScene(self):
        self._initiated = True
        self.start = time.time()
        self.position = (0, 0)
        self.opacity = 1.0
        self.gameobjects = []