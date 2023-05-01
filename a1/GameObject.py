from a1.SpriteTools import SpriteTools
from a1.a1Enums import Alignment, SpriteDirection
from a1.Lerp_Laundmo import Lerp
from a1.a1Time import a1Time
from a1.ScreenSize import ScreenSize
import pygame
import math
from a1.a1Math import Normalize

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
        self.name = name
        self.alignment = alignment
        
        self.spriteobject = None
        self.textobject = None
        # position
        self.oldPosition = None
        self.position = startpos
        # scale
        self.oldScale = None
        self.scale = 1.0
        # opacity
        self.oldOpacity = None
        self.opacity = 1.0
        # text message
        self.oldText = None
        self.textMessage = ""
        # text color
        self.oldTextColor = None
        self.textColor = (0, 0, 0)
        # rotation
        self.oldRotation = None
        self.rotation = 0

        # debugging
        self.showCollider = False
        self.debugColor = (255, 0, 0)
    

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
        self.setTextColor(newTextObj.color)
        self.updateText(newTextObj.message)

    def setTextColor(self, color):
        self.textColor = color
        
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

    def setRotation(self, degrees):
        self.rotation = degrees
        
    def pointIsColliding(self, point):
        if self.spriteobject != None:
            if self.spriteobject.sprite.rect.collidepoint(point):
                return True
        if self.textobject != None:
            if self.textobject.rect.collidepoint(point):
                return True
        return False

    def update(self):
        pass

    def moveTowards(self, targetpos, pixelsToMove):
        mypos = self.position
        lookVector = (targetpos[0] - mypos[0], targetpos[1] - mypos[1])
        normalizedVec = Normalize(lookVector)

        newX = mypos[0] + normalizedVec[0] * pixelsToMove * a1Time.DeltaTime
        newY = mypos[1] + normalizedVec[1] * pixelsToMove * a1Time.DeltaTime

        self.position = (newX, newY)

    def lookAt(self, targetpos, imgdir : SpriteDirection = SpriteDirection.North):
        mypos = self.position
        lookVector = (targetpos[0] - mypos[0], -(targetpos[1] - mypos[1]))
        
        zRadians = math.atan2(lookVector[1], lookVector[0])
        zRot = (zRadians / math.pi) * 180

        imgdir_val = imgdir.value[0]
        direction_compensation = 90 * imgdir_val
        zRot -= direction_compensation

        self.setRotation(zRot)

    def draw(self, screen, scene):
        
        if self.spriteobject != None:

            if self.oldScale != self.scale:
                SpriteTools.setSpriteScale(self.spriteobject, self.scale)

            if self.oldPosition != self.position or self.oldRotation != self.rotation:
                SpriteTools.setSpritePos(self.spriteobject, self.position, scene, self.alignment, self.scale, self.rotation)

            if self.oldOpacity != self.opacity:
                SpriteTools.setSpriteOpacity(self.spriteobject, self.opacity, scene)

            screen.blit(self.spriteobject.sprite.image, self.spriteobject.sprite.rect)
            # Debug hitbox:
            if self.showCollider == True:
                pygame.draw.rect(screen, self.debugColor, self.spriteobject.sprite.rect, 4)


        if self.textobject != None:
            # set message first so we can manipulate it after
            if self.oldText != self.textMessage:
                SpriteTools.setTextMessage(self.textobject, self.textMessage)
                SpriteTools.setTextScale(self.textobject, self.scale)

            # set color
            if self.oldTextColor != self.textColor:
                SpriteTools.setTextColor(self.textobject, self.textColor)
                # Setting color resets rotation so we unfortunately need to trigger rotation set
                self.oldRotation = None

            # set scale 
            if self.oldScale != self.scale:
                SpriteTools.setTextScale(self.textobject, self.scale)

            # set position and/or rotation
            if self.oldPosition != self.position or self.oldRotation != self.rotation:
                SpriteTools.setTextPos(self.textobject, self.position, scene, self.alignment, self.scale, self.rotation)
            
            # Opacity has to be last because changing the scale overrides the surface so
            # it overrides Opacity if Opacity gets set first
            if self.oldOpacity != self.opacity:
                SpriteTools.setTextOpacity(self.textobject, self.opacity, scene)
                
            screen.blit(self.textobject.surf, self.textobject.rect)
            # Debug hitbox:
            if self.showCollider == True:
                pygame.draw.rect(screen, (self.debugColor[0]*0.5, self.debugColor[1]*0.5, self.debugColor[2]*0.5), self.textobject.rect, 2)

        self.oldPosition = self.position
        self.oldRotation = self.rotation
        self.oldScale = self.scale
        self.oldOpacity = self.opacity
        self.oldText = self.textMessage
        self.oldTextColor = self.textColor

    def onDestroy(self):
        pass




    
    

