from a1.SpriteTools import SpriteTools
from a1.a1Enums import Alignment
from a1.Lerp_Laundmo import Lerp
from a1.a1Time import a1Time

class GameObject():
    
    def height(self):
        if self.spriteobject != None and self.textobject != None:
            sHeight = self.spriteobject.sprite.image.get_size()[1] #* self.scale
            tHeight = self.textobject.surf.get_size()[1] #* self.scale

            if sHeight > tHeight:
                return sHeight
            else:
                return tHeight

        elif self.spriteobject != None:
            return self.spriteobject.sprite.image.get_size()[1] #* self.scale

        elif self.textobject != None:
            return self.textobject.surf.get_size()[1] #* self.scale

        else:
            return 0.0

    def width(self):
        if self.spriteobject != None and self.textobject != None:
            sWidth = self.spriteobject.sprite.image.get_size()[0] #* self.scale
            tWidth = self.textobject.surf.get_size()[0] #* self.scale

            if sWidth > tWidth:
                return sWidth
            else:
                return tWidth

        elif self.spriteobject != None:
            return self.spriteobject.sprite.image.get_size()[0] #* self.scale

        elif self.textobject != None:
            return self.textobject.surf.get_size()[0] #* self.scale

        else:
            return 0.0


    def __init__(self, startpos, name = "noname", alignment = Alignment.Center):
        self.position = startpos
        self.name = name
        self.alignment = alignment

        self.oldScale = 1.0
        self.scale = 1.0
        self.oldOpacity = 1.0
        self.opacity = 1.0
        self.spriteobject = None
        self.textobject = None
        self.oldText = ""
        self.textMessage = ""

        # online stuff
        self.lerpFloat = 0.0
        self.lerping = False
        self.frompos = (0, 0)
        self.targetpos = (0, 0)
    
    def addSprite(self, spriteobject):
        self.spriteobject = spriteobject
        self.oldScale = -1

    def setOpacity(self, newopacity):
        self.opacity = newopacity
        #print("opacity: {} newop: {}".format(self._name, newopacity))
        
    def updateText(self, newMessage : str):
        self.textMessage = newMessage
        
    def addText(self, newTextObj):
        self.textobject = newTextObj
        self.updateText(newTextObj.message)
        
    def setPosition(self, pos, lerped : bool = False):
        if (lerped):
            self.lerping = True
            self.frompos = self.position
            self.targetpos = pos
            self.lerpFloat = 0.0
        else:
            self.position = pos


    def setScale(self, newscale):
        self.scale = newscale
        #print("scale: {} newscale: {}".format(self, newscale))
        

    def update(self):
        pass

    def draw(self, screen, scene):
        
        if (self.spriteobject is not None):

            if self.oldOpacity != self.opacity:
                self.oldOpacity = self.opacity
                SpriteTools.setSpriteOpacity(self.spriteobject, self.oldOpacity, scene)

            if self.oldScale != self.scale:
                self.oldScale = self.scale
                SpriteTools.setSpriteScale(self.spriteobject, self.oldScale)

            SpriteTools.setSpritePos(self.spriteobject, self.position, scene, self.alignment)

            screen.blit(self.spriteobject.sprite.image, self.spriteobject.sprite.rect)
            #pygame.draw.rect(screen, (0, 0, 255), self.spriteobject.sprite.rect, 4)


        if (self.textobject is not None):
            # set message first so we can manipulate it after
            if self.oldText != self.textMessage:
                self.oldText = self.textMessage
                SpriteTools.setTextMessage(self.textobject, self.oldText)
                SpriteTools.setTextScale(self.textobject, self.oldScale)
            # set scale if we didnt already do so above ^
            if self.oldScale != self.scale:
                self.oldScale = self.scale
                SpriteTools.setTextScale(self.textobject, self.oldScale)
            # set pos after setting scale in case the scale moves the origin by a tiny amount
            SpriteTools.setTextPos(self.textobject, self.position, scene, self.alignment)
            # Opacity has to be last because changing the scale overrides the surface so
            # it overrides Opacity if Opacity gets set first
            if self.oldOpacity != self.opacity:
                self.oldOpacity = self.opacity
                SpriteTools.setTextOpacity(self.textobject, self.oldOpacity, scene)
            # this is a debug thing, keep to remember how!!
            screen.blit(self.textobject.surf, self.textobject.rect)
            #pygame.draw.rect(screen, (5, 255, 255), self.textobject.rect, 3)


    
    
