from a1.Scene import Scene
from a1.GameObject import Alignment, GameObject
from a1.SpriteTools import SpriteTools
from a1.ScreenSize import ScreenSize


class BackgroundScene(Scene):

    def InitScene(self):
        super().InitScene()
        
        backgroundImage = GameObject(ScreenSize.Center(), "background", Alignment.Center)
        self.addGameObject(backgroundImage)
        backgroundImage.addSprite(SpriteTools.getSprite("img/test.png"))

        






