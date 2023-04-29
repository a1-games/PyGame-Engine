from a1.GameObject import GameObject
from a1.SpriteTools import SpriteTools
from a1.Scene import Scene
from a1.a1Time import a1Time
from a1.GameObject import Alignment


class DebugScene(Scene):
    def InitScene(self):
        super().InitScene()
        
        self.fpscounter = GameObject((4, 4), alignment = Alignment.TopLeft)
        self.addGameObject(self.fpscounter)
        self.frameRateText = SpriteTools.getTextRect("fps: {}".format(a1Time.Fps), (255, 255, 0))
        self.fpscounter.addText(self.frameRateText)
        self.fpscounter.setScale(0.4)

    def update(self, mousepos):
        super().update(mousepos)
        self.fpscounter.updateText("fps: {}".format(a1Time.Fps))

