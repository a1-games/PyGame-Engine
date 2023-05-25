import abc
import time
import pygame
from a1.GameObject import GameObject
from a1.a1Debug import a1Debug
from a1.Button import Button
from a1.MousePos import MousePos

class Scene(metaclass=abc.ABCMeta):

    clicked = False
    clicks = []

    def disable(self):
        self._active = False


    def setPosition(self, pos):
        if self._initiated == False:
            a1Debug.Log("ERROR: Setting scene position before scene was initiated!")
            return
        self.position = pos
        for gameobject in self.gameobjects:
            gameobject.oldPosition = None            

    def setOpacity(self, opacity):
        if self._initiated == False:
            a1Debug.Log("ERROR: Setting scene opacity before scene was initiated!")
            return
        self.opacity = opacity
        for gameobject in self.gameobjects:
            gameobject.oldOpacity = None

    def addGameObject(self, gameobject : GameObject):
        self.gameobjects.append(gameobject)

    def addButton(self, button):
        self.buttons.append(button)

    def destroyButton(self, button : Button):
        self.buttons.remove(button)
        self.destroyGameObject(button)

    def destroyGameObject(self, gameobject : GameObject):
        gameobject.onDestroy(self)
        self.gameobjects.remove(gameobject)
        del gameobject

    def destroyGameObjectByName(self, gameobjectname : str):
        for gameobject in self.gameobjects:
            if gameobject.name == gameobjectname:
                gameobject.onDestroy(self)
                self.gameobjects.remove(gameobject)
                del gameobject

    def draw(self, screen):
        #a1Debug.Log("is drawing")
        for gameobject in self.gameobjects:
            #a1Debug.Log("is drawing a spriterect in spriterects")
            if gameobject.active:
                gameobject.draw(screen, self)

    def update(self):

        #a1Debug.Log("is drawing")
        if not GameObject._paused:
            for gameobject in self.gameobjects:
                #a1Debug.Log("is drawing a spriterect in spriterects")
                if gameobject.active:
                    gameobject.update()

        if self._handleEvents:
            self.checkHovering()

    
    def checkHovering(self):
        for button in self.buttons:
            if button.active:
                if not button.onPointerEnter.isEmpty() and not button.onPointerExit.isEmpty():
                    button.checkPointerExit(MousePos())
        for button in self.buttons:
            if button.active:
                if not button.onPointerEnter.isEmpty() and not button.onPointerExit.isEmpty():
                    button.checkPointerEnter(MousePos())
            

    def handleEvents(self, events):
        if self._handleEvents:
            # handle events
            for event in events:
                # This defines a mouseclick listener
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        # If we clicked the collider of playButton
                        if button.active and not Scene.clicked:
                            if button.pointIsColliding(MousePos()):
                                Scene.clicks.append(button)
                                #button.isDown = True
                                #Scene.clicked = True
                                #button.onClick.invoke()
                # This defines a mouseup listener
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        # If we clicked the collider of playButton
                        if button.active:
                            if button.isDown:
                                button.isDown = False
                                button.onRelease.invoke()
        

    def InitScene(self):
        self._initiated = True
        self._active = True
        self._handleEvents = True
        self.mousepos = (0, 0)
        self.start = time.time()
        self.position = (0, 0)
        self.opacity = 1.0
        self.gameobjects = []
        self.buttons = []