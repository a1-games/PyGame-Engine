from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.MousePos import MousePos
from a1.SpriteTools import SpriteTools, TextObject
from a1.Scene import Scene

class CursorInfo():

    _active = False
    cursorInfoGameObject = None

    def setCursorInfoGameObject(cito : GameObject):
        CursorInfo.cursorInfoGameObject = cito

    @staticmethod
    def setInfoText(info : str):
        CursorInfo.cursorInfoGameObject.updateText(info)
        CursorInfo._active = True

    @staticmethod
    def hide():
        CursorInfo._active = False


class CursorInfoScene(Scene):

    def InitScene(self):
        super().InitScene()
        infoObject = GameObject((0, 0), "cursorInfoGameObject", Alignment.BottomLeft)
        infoObject.addText(SpriteTools.getTextRect("Info", (255, 255, 0)))
        infoObject.setScale(0.4)
        self.addGameObject(infoObject)

        CursorInfo.setCursorInfoGameObject(infoObject)
        CursorInfo._active = False



    def draw(self, screen):
        if not CursorInfo._active: 
            return
        super().draw(screen)

    def update(self):
        if not CursorInfo._active: 
            return
        super().update()
        
        CursorInfo.cursorInfoGameObject.setPosition(MousePos())

