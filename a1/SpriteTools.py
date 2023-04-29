from a1.a1Enums import Alignment
import pygame

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class TextObject():
    message = ""
    color = (255, 255, 255)
    surf = None
    rect = None
    surf_origin = None

    def __init__(self, message, color, surf, rect):
        self.message = message
        self.color = color
        self.surf = surf
        self.surf_origin = surf
        self.rect = rect

class SpriteObject():
    sprite = None
    # is named img as to not be confused with sprite.image
    img = None

    def __init__(self, sprite, img):
        self.sprite = sprite
        self.img = img


class SpriteTools():

    _fontsize = 48

    @staticmethod
    def setSpritePos(spriteobject, pos, scene, alignment : Alignment):
        w_x = spriteobject.sprite.rect.width
        w_y = spriteobject.sprite.rect.height

        posX = scene.position[0] + pos[0]
        posY = scene.position[1] + pos[1]

        if alignment == Alignment.TopLeft:
            spriteobject.sprite.rect.x = posX
            spriteobject.sprite.rect.y = posY
        elif alignment == Alignment.TopRight:
            spriteobject.sprite.rect.x = posX - w_x
            spriteobject.sprite.rect.y = posY
        elif alignment == Alignment.BottomLeft:
            spriteobject.sprite.rect.x = posX
            spriteobject.sprite.rect.y = posY - w_y
        elif alignment == Alignment.BottomRight:
            spriteobject.sprite.rect.x = posX - w_x
            spriteobject.sprite.rect.y = posY - w_y
        else: # if alignment is center
            spriteobject.sprite.rect.center = (posX, posY)
            #spriteobject.sprite.rect.x = posX - w_x / 2
            #spriteobject.sprite.rect.y = posY - w_y / 2

    @staticmethod
    def setSpriteScale(spriteobject, scale):
        spriteobject.sprite.image = pygame.transform.smoothscale_by(spriteobject.img, scale)
        size = spriteobject.sprite.image.get_size()
        spriteobject.sprite.rect.width = size[0]
        spriteobject.sprite.rect.height = size[1]

    @staticmethod
    def setSpriteOpacity(spriteobject, opacity, scene):
        alpha = opacity * scene.opacity * 255
        if alpha > 255:
            alpha = 255
        spriteobject.img.set_alpha(alpha)
        #print("setting opacity to {}".format(opacity))
        spriteobject.sprite.image = spriteobject.img
        #print(spriterect[1].get_alpha())

    @staticmethod
    def getSprite(imagename, scene = None):

        path = resource_path(imagename)
        img = pygame.image.load(path)
        sprite = pygame.sprite.Sprite()
        sprite.rect = img.get_rect()
        sprite.image = img

        spriteobject = SpriteObject(sprite, img)

        #pos = (0, 0)
        #SpriteTools.setSpritePos(spriteobject, pos, scene)

        return spriteobject
    

    @staticmethod
    def setTextPos(textobject : TextObject, pos, scene, alignment : Alignment):
        w_x = textobject.rect.width
        w_y = textobject.rect.height
        
        posX = scene.position[0] + pos[0]
        posY = scene.position[1] + pos[1]

        if alignment == Alignment.TopLeft:
            textobject.rect.x = posX
            textobject.rect.y = posY
        elif alignment == Alignment.TopRight:
            textobject.rect.x = posX - w_x
            textobject.rect.y = posY
        elif alignment == Alignment.BottomLeft:
            textobject.rect.x = posX
            textobject.rect.y = posY - w_y
        elif alignment == Alignment.BottomRight:
            textobject.rect.x = posX - w_x
            textobject.rect.y = posY - w_y
        else: # if alignment is center
            textobject.rect.center = (posX, posY)
        
    @staticmethod
    def setTextMessage(textobject : TextObject, newMessage : str):
        textobject.message = newMessage
        surf = SpriteTools._renderFontToSurface(textobject.color, newMessage)
        textobject.surf = surf
        textobject.surf_origin = surf
        
    @staticmethod
    def setTextColor(textobject : TextObject, newColor):
        textobject.color = newColor
        surf = SpriteTools._renderFontToSurface(textobject.color, textobject.message)
        textobject.surf = surf
        textobject.surf_origin = surf

    @staticmethod
    def _renderFontToSurface(color, message):
        font = pygame.sysfont.SysFont(None, SpriteTools._fontsize)
        surf = font.render(message, True, color)
        return surf

    @staticmethod
    def setTextScale(textobject : TextObject, scale):
        textobject.surf = pygame.transform.smoothscale_by(textobject.surf_origin, scale)
        size = textobject.surf.get_size()
        textobject.rect.width = size[0]
        textobject.rect.height = size[1]


    @staticmethod
    def getTextRect(message : str, color):
        surf = SpriteTools._renderFontToSurface(color, message)
        rect = surf.get_rect()

        #pos = (0, 0)

        textobject = TextObject(message, color, surf, rect)
        # these two methods are called every frame by GameObject so they wont work in here any more
        #SpriteTools.setTextScale(textobject, startScale)
        #SpriteTools.setTextPos(textobject, pos, scene)

        return textobject
    
    @staticmethod
    def setTextOpacity(textobject : TextObject, opacity, scene):
        alpha = opacity * scene.opacity * 255
        if alpha > 255:
            alpha = 255
        textobject.surf.set_alpha(alpha)

