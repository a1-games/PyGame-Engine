import pygame
from a1.GameObject import GameObject
from a1.SpriteTools import SpriteTools
from a1.Scene import Scene
from a1.a1Time import a1Time
from a1.GameObject import Alignment
from a1.ScreenSize import ScreenSize
from a1.SceneManager import SceneManager, SceneTransition


class MainScene(Scene):

    mousepos = (0, 0)

    def InitScene(self):
        super().InitScene()

        self.playButton = GameObject(ScreenSize.Center(), "background", Alignment.Center)
        self.addGameObject(self.playButton)
        self.playButton.addText(SpriteTools.getTextRect(("Start Game"), (255, 255, 255)))

        
    def update(self):
        super().update()
        # We also use mousepos in events so we set it here as to not call the get() multiple times per frame
        self.mouse_pos = pygame.mouse.get_pos()

        if self.playButton.pointIsColliding(self.mouse_pos):
            self.playButton.setTextColor((255, 255, 0))
        else:
            self.playButton.setTextColor((255, 255, 255))
    
        
    def handleEvents(self, events):
        # super does not handle events, super() not needed
        for event in events:
            # This defines a mouseclick listener
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If we clicked the collider of playButton
                if self.playButton.pointIsColliding(self.mouse_pos):
                    # Uncomment and use your own scene to get started
                    # SceneManager.replaceScene("MainLayer", YourScene(), SceneTransition.Slide_L2R)
                    pass

                





