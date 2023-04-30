import pygame
import math
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
        #self.playButton.addSprite(SpriteTools.getSprite(("img/testbanner.png"), self))
        self.playButton.addText(SpriteTools.getTextRect(("Start Game"), (255, 255, 255)))
        # Change the empty scene to your own scene
        self.playButton.onClick = lambda : self.changeScene(EmptyScene())
        self.playButton.onPointerEnter = lambda : self.playButton.setTextColor((255, 255, 0))
        self.playButton.onPointerExit = lambda : self.playButton.setTextColor((255, 255, 255))

        #self.playButton.showCollider = True


    def update(self, mousepos):
        super().update(mousepos)

        #self.playButton.setRotation(self.playButton.rotation + 0.1)





