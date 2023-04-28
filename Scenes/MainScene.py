from a1.GameObject import GameObject
from a1.SpriteTools import SpriteTools
from a1.Scene import Scene
from a1.a1Time import a1Time
from a1.GameObject import Alignment
from a1.ScreenSize import ScreenSize


class MainScene(Scene):
    def InitScene(self):
        super().InitScene()

        backgroundImage = GameObject(ScreenSize.Center(), "background", Alignment.Center)
        self.addGameObject(backgroundImage)
        backgroundImage.addSprite(SpriteTools.getSprite("img/test.png"))

        

    def update(self):
        super().update()

