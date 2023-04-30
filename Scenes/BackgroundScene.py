from a1.Scene import Scene
from a1.GameObject import Alignment, GameObject
from a1.SpriteTools import SpriteTools
from a1.ScreenSize import ScreenSize


class BackgroundScene(Scene):

    def InitScene(self):
        super().InitScene()
        
        backgroundImage = GameObject((200, 200), "background", Alignment.Center)
        self.addGameObject(backgroundImage)
        backgroundImage.addSprite(SpriteTools.getSprite("img/testbanner.png"))
        
        backgroundImage2 = GameObject((600, 200), "background", Alignment.Center)
        self.addGameObject(backgroundImage2)
        backgroundImage2.addSprite(SpriteTools.getSprite("img/testbanner.png"))

    def draw(self, screen):
        screen.fill((0, 0, 0))
        super().draw(screen)


