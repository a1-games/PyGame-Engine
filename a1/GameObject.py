from a1.SpriteTools import SpriteTools
from a1.a1Enums import Alignment, SpriteDirection
from a1.Lerp import Lerp
from a1.a1Time import a1Time
from a1.ScreenSize import ScreenSize
from a1.a1Debug import a1Debug
import pygame
import math
from a1.a1Math import Normalize

class GameObject():

    _paused = False
    @staticmethod
    def PauseGameObjects():
        GameObject._paused = True
    @staticmethod
    def UnpauseGameObjects():
        GameObject._paused = False
    
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


    def setActive(self, bool : bool):
        self.active = bool

    def toggleActive(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def __init__(self, startpos : tuple = (0, 0), name = "noname", spritealignment = Alignment.Center, textalignment : Alignment = None, textIsRelative : bool = False):
        self.name = name
        self.setAlignment(spritealignment, textalignment)
        self.active = True
        self.started = False
        
        self.spriteobject = None
        self.textobject = None
        # position
        self.oldPosition = None
        self.oldTextPosition = None
        self.setPosition(startpos, textIsRelative)
        # scale
        self.oldScale = 1.0
        self.scale = 1.0
        # opacity
        self.oldOpacity = 1.0
        self.opacity = 1.0
        # text message
        self.oldText = None
        self.textMessage = ""
        # text color
        self.oldTextColor = None
        self.textColor = (0, 0, 0)
        # rotation
        self.oldRotation = None
        self.rotation = -1

        # debugging
        self.showCollider = True
        self.debugColor = (255, 0, 0)


    def start(self, scene):
        scene.doNextFrame.put(lambda : self.setPosition(self.position, self.textIsRelative))
    

    def addSprite(self, spriteobject):
        self.spriteobject = spriteobject
        self.oldScale = -1
        self.setPosition(self.position, self.textIsRelative)
        

    def replaceSpriteImg(self, newImg):
        self.spriteobject.replaceImg(newImg)
        # setting scale causes the image loading to refresh. without it, it wouldn't change until the next time this happens.
        self.oldScale = None

    def setOpacity(self, newopacity):
        self.opacity = newopacity
        #a1Debug.Log("opacity: {} newop: {}".format(self._name, newopacity))
        
    def updateText(self, newMessage : str):
        self.textMessage = newMessage
        
    def addText(self, newTextObj):
        self.textobject = newTextObj
        self.setTextColor(newTextObj.color)
        self.updateText(newTextObj.message)

    def setTextColor(self, color):
        self.textColor = color

    def setPosition(self, pos, textIsRelative : bool = False, lerped : bool = False):
        self.textIsRelative = textIsRelative
        if not lerped:
            self.position = pos
            self.textposition = pos
            if textIsRelative:
                self.setRelativeTextPos()

        # ignore this, it is a leftover from a networked adaptation that i want to get back to
        else:
            self.lerping = True
            self.frompos = self.position
            self.targetpos = pos
            self.lerpFloat = 0.0

    def setRelativeTextPos(self):
        if self.spriteobject != None:
            # this code is correct but it happens before the rect has its position set. find a solution!!!
            rect = self.spriteobject.sprite.rect
            if self.textalignment == Alignment.Center:
                self.textposition = rect.center
                # we dont use x/y so just get out of here
                return
            
            x = rect.x
            y = rect.y
            # get the alignment point of the sprite rect
            if self.textalignment == Alignment.TopMiddle:
                x += rect.width/2
            if self.textalignment == Alignment.TopRight:
                x += rect.width
            if self.textalignment == Alignment.RightMiddle:
                x += rect.width
                y += rect.height/2
            if self.textalignment == Alignment.BottomRight:
                x += rect.width
                y += rect.height
            if self.textalignment == Alignment.BottomMiddle:
                x += rect.width/2
                y += rect.height
            if self.textalignment == Alignment.BottomLeft:
                y += rect.height
            if self.textalignment == Alignment.LeftMiddle:
                y += rect.height/2
            # top left is default

            # set pos
            self.textposition = (x, y)
            #a1Debug.LogRainbow(self.name + " " + str((x, y)))



    def setScale(self, newscale):
        self.scale = newscale
        #a1Debug.Log("scale: {} newscale: {}".format(self, newscale))

    def setAlignment(self, spritealign : Alignment, textalign : Alignment = None):
        self.spritealignment = spritealign
        if textalign == None:
            self.textalignment = spritealign
        else:
            self.textalignment = textalign

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
                SpriteTools.setSpritePos(self.spriteobject, self.position, scene, self.spritealignment, self.scale, self.rotation)
                if self.opacity != 1:
                    self.oldOpacity = None

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
            if self.oldPosition != self.position or self.oldRotation != self.rotation or self.oldTextPosition != self.textposition:
                SpriteTools.setTextPos(self.textobject, self.textposition, scene, self.textalignment, self.scale, self.rotation)
            
            # set opacity
            if self.oldOpacity != self.opacity:
                SpriteTools.setTextOpacity(self.textobject, self.opacity, scene)
                
            screen.blit(self.textobject.surf, self.textobject.rect)
            # Debug hitbox:
            if self.showCollider == True:
                pygame.draw.rect(screen, (self.debugColor[0]*0.5, self.debugColor[1]*0.5, self.debugColor[2]*0.5), self.textobject.rect, 2)

        self.oldPosition = self.position
        self.oldTextPosition = self.textposition
        self.oldRotation = self.rotation
        self.oldScale = self.scale
        self.oldOpacity = self.opacity
        self.oldText = self.textMessage
        self.oldTextColor = self.textColor

    def onDestroy(self, scene):
        pass




    
    

