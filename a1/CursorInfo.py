from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.MousePos import MousePos
from a1.SpriteTools import SpriteTools, TextObject
from a1.Scene import Scene

class CursorInfo():

    text_active = False
    cursor_active = False
    cursorInfoGameObject = None
    cursorImageGameObject = None
    defaultCursorImage = None

    def setCursorInfoGameObject(cito : GameObject):
        CursorInfo.cursorInfoGameObject = cito

    def setCursorImageObject(ci : GameObject):
        CursorInfo.cursorImageGameObject = ci

    # The cursor image must be 16x16
    def setDefaultCursor(image):
        CursorInfo.defaultCursorImage = image
    @staticmethod
    # The cursor image must be 16x16
    def setCursorImage(image : str, hideText : bool = False):
        CursorInfo.cursorImageGameObject.replaceSpriteImg(image)
        CursorInfo.cursor_active = True
        if hideText:
            CursorInfo.text_active = False


    @staticmethod
    def setInfoText(info : str, hideCursor : bool = True):
        CursorInfo.cursorInfoGameObject.updateText(info)
        CursorInfo.text_active = True
        if hideCursor:
            CursorInfo.cursor_active = False

    @staticmethod
    def hide():
        CursorInfo.cursorInfoGameObject.updateText("")
        CursorInfo.text_active = False
        CursorInfo.cursor_active = False


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
        CursorInfo.cursor_active = False
        CursorInfo.text_active = False


    def draw(self, screen):
        if CursorInfo.cursor_active: 
            CursorInfo.cursorImageGameObject.draw(screen, self)
        
        if CursorInfo.text_active: 
            CursorInfo.cursorInfoGameObject.draw(screen, self)


    def update(self):
        if not CursorInfo.cursor_active and not CursorInfo.text_active: 
            return
        super().update()
        
        CursorInfo.cursorInfoGameObject.setPosition(MousePos())
        CursorInfo.cursorImageGameObject.setPosition(MousePos())

