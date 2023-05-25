from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.a1Events import a1Event
from a1.MousePos import MousePos
from a1.a1Debug import a1Debug
from a1.Button import Button
from a1.SpriteTools import SpriteTools


class Slider(GameObject):

    def __init__(self, startpos, scene, name="slider", alignment=Alignment.Center):
        super().__init__(startpos, name, alignment)
        # background
        self.background = GameObject(startpos, "sliderfill", alignment=Alignment.Center)
        self.background.addSprite(SpriteTools.getSprite("img/slider_background.png"))
        scene.addGameObject(self.background)

        # fill
        self.fill = GameObject(startpos, "sliderfill", alignment=Alignment.BottomLeft)
        self.fill.addSprite(SpriteTools.getSprite("img/slider_fill.png"))
        scene.addGameObject(self.fill)

        # values
        self.onValueChanged = a1Event()
        self.dragging = False
        self.min = self.position[0] - self.background.width() / 2
        self.max = self.position[0] + self.background.width() / 2
        self.setValue(1)

        # handle
        handleimg = SpriteTools.getSprite("img/slider_handle.png").img
        handleimg_hover = SpriteTools.getSprite("img/slider_handle_highlighted.png").img

        self.handle = Button(startpos, scene, "sliderhandle")
        self.handle.addSprite(SpriteTools.getSprite("img/slider_handle.png"))
        scene.addGameObject(self.handle)
        self.handle.onClick.addListener(lambda : self.drag())
        self.handle.onRelease.addListener(lambda : self.stopdrag())
        self.handle.onPointerEnter.addListener(lambda : self.handle.replaceSpriteImg(handleimg_hover))
        self.handle.onPointerExit.addListener(lambda : self.handle.replaceSpriteImg(handleimg))

        self.setPosition(startpos)

 
    def setRotation(self, degrees):
        a1Debug.LogWarning("Rotation is not possible on built-in sliders.")

    def setActive(self, bool: bool):
        self.background.setActive(bool)
        self.fill.setActive(bool)
        self.handle.setActive(bool)
        super().setActive(bool)

    def setPosition(self, pos, lerped: bool = False):
        super().setPosition(pos, lerped)
        self.fill.setPosition((pos[0] - self.background.width()/2, pos[1] + self.background.height() / 2))
        self.handle.setPosition((self.max, self.handle.position[1]))


    def setScale(self, newscale):
        super().setScale(newscale)
        self.background.setScale(newscale)
        self.fill.setScale((self.fill.scale[0] * newscale, newscale))
        self.handle.setScale(newscale)
        self.min = self.position[0] - self.background.width() / 2 * newscale
        self.max = self.position[0] + self.background.width() / 2 * newscale
        self.fill.setPosition((self.position[0] - self.background.width()/2 * newscale, self.position[1] + self.background.height() / 2 * newscale))
        self.handle.setPosition((self.max, self.handle.position[1]))


    def drag(self):
        self.dragging = True
    def stopdrag(self):
        self.dragging = False


    def setValue(self, value : float):
        self.fill.setScale((self.scale * value, self.scale))
        self.value = value
        self.onValueChanged.invoke(value)


    def update(self):
        super().update()

        if self.dragging:
            mp = MousePos()[0]
            val = (mp - self.min) / (self.max - self.min)
            if self.min < mp and mp < self.max:
                self.handle.setPosition((MousePos()[0], self.handle.position[1]))
                self.setValue(val)




    
    def onDestroy(self, scene):
        scene.destroyGameObject(self.fill)
        scene.destroyGameObject(self.handle)
        scene.destroyGameObject(self.background)
        return super().onDestroy(scene)
    


