import pygame
from a1.GameObject import GameObject
from a1.SpriteTools import SpriteTools
from a1.Scene import Scene
from a1.a1Time import a1Time
from a1.GameObject import Alignment
from a1.Button import Button
from a1.ScreenSize import ScreenSize
from Scenes.EmptyScene import EmptyScene
from a1.SceneManager import SceneManager, SceneTransition


class MainScene(Scene):

    mousepos = (0, 0)

    def changeScene(self, scene : Scene):
        SceneManager.replaceScene("MainLayer", scene, SceneTransition.CrossFade)


    def InitScene(self):
        super().InitScene()

        self.playButton = Button(ScreenSize.Center(), self, print("test"))
        self.addGameObject(self.playButton)
        self.playButton.addText(SpriteTools.getTextRect(("Start Game"), (255, 255, 255)))
        # Change the empty scene to your own scene
        self.playButton.onClick = lambda : self.changeScene(EmptyScene())

        
    def update(self):
        super().update()
        # We also use mousepos in events so we set it here as to not call the get() multiple times per frame
        self.mouse_pos = pygame.mouse.get_pos()

        if self.playButton.pointIsColliding(self.mouse_pos):
            self.playButton.setTextColor((255, 255, 0))
        else:
            self.playButton.setTextColor((255, 255, 255))
    
        
                





