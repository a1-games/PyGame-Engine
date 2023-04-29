import abc
import time
import pygame
from a1.GameObject import GameObject

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

    def addGameObject(self, gameobject : GameObject):
        self.gameobjects.append(gameobject)

    def addButton(self, button):
        self.buttons.append(button)

    def removeButton(self, button):
        self.buttons.remove(button)

    def destroyGameObject(self, gameobject : GameObject):
        gameobject.onDestroy()
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
        for event in events:
            # This defines a mouseclick listener
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for button in self.buttons:
                    # If we clicked the collider of playButton
                    if button.pointIsColliding(mousepos):
                        button.onClick()

    def InitScene(self):
        self._initiated = True
        self.start = time.time()
        self.position = (0, 0)
        self.opacity = 1.0
        self.gameobjects = []
        self.buttons = []