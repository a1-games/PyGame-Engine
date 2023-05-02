from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.MousePos import MousePos
from a1.SpriteTools import SpriteTools
from a1.Scene import Scene

class CursorInfo():

    _active = False
    cursorInfoTextObject = None

    def setCursorInfoTextObject(cito):
        CursorInfo.cursorInfoTextObject = cito

    @staticmethod
    def setInfoText(info):
        CursorInfo.cursorInfoTextObject.updateText(info)
        CursorInfo._active = True

    @staticmethod
    def hide():
        CursorInfo._active = False


class CursorInfoScene(Scene):

    def InitScene(self):
        super().InitScene()
        infoObject = GameObject((0, 0), "CursorInfoTextObject", Alignment.BottomLeft)
        infoObject.addText(SpriteTools.getTextRect("Info", (255, 255, 0)))
        infoObject.setScale(0.4)
        self.addGameObject(infoObject)

        CursorInfo.setCursorInfoTextObject(infoObject)
        CursorInfo._active = False



    def draw(self, screen):
        if not CursorInfo._active: 
            return
        super().draw(screen)

    def update(self):
        if not CursorInfo._active: 
            return
        super().update()
        
        CursorInfo.cursorInfoTextObject.setPosition(MousePos())

