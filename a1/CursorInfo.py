from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.MousePos import MousePos
from a1.SpriteTools import SpriteTools, TextObject
from a1.Scene import Scene

class CursorInfo():

    _active = False
    cursorInfoGameObject = None
    cursorImageGameObject = None
    defaultCursorImage = None

    def setCursorInfoGameObject(cito : GameObject):
        CursorInfo.cursorInfoGameObject = cito

    def setCursorImageObject(ci : GameObject):
        CursorInfo.cursorImageGameObject = ci

    @staticmethod
    # The cursor image must be 16x16
    def setCursorImage(image : str):
        CursorInfo.cursorImageGameObject.replaceSpriteImg(image)
        CursorInfo._active = True

    # The cursor image must be 16x16
    def setDefaultCursor(image):
        CursorInfo.defaultCursorImage = image

    @staticmethod
    def setInfoText(info : str):
        CursorInfo.cursorInfoGameObject.updateText(info)
        CursorInfo._active = True

    @staticmethod
    def hide():
        CursorInfo.cursorInfoGameObject.updateText("")
        CursorInfo._active = False


class CursorInfoScene(Scene):

    def InitScene(self):
        super().InitScene()
        infoObject = GameObject((0, 0), "cursorInfoGameObject", Alignment.BottomLeft)
        infoObject.addText(SpriteTools.getTextRect("Info", (255, 255, 0)))
        infoObject.setScale(0.4)
        self.addGameObject(infoObject)
        
        CursorInfo.setDefaultCursor(SpriteTools.getSprite("img/empty.png", self).img)
        cursorObject = GameObject((0, 0), "cursorImageGameObject", Alignment.BottomRight)
        cursorObject.addSprite(SpriteTools.getSprite("img/empty.png", self))
        self.addGameObject(cursorObject)

        CursorInfo.setCursorInfoGameObject(infoObject)
        CursorInfo.setCursorImageObject(cursorObject)
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
        CursorInfo.cursorImageGameObject.setPosition(MousePos())

