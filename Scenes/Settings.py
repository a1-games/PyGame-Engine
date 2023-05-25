from a1.Scene import Scene
from a1.ScreenSize import ScreenSize
from a1.SpriteTools import SpriteTools
from a1.GameObject import GameObject, Alignment
from a1.Button import Button
from a1.Slider import Slider
from a1.JukeBox import JukeBox
from a1.SceneManager import SceneManager
from a1.a1Time import a1Time
import pygame


class Settings(Scene):
    def InitScene(self):
        super().InitScene()

        
        # -- SETTINGS --
        

        self.volumeslider = Slider(ScreenSize.Center_OffH(200), self, "test slider")
        self.addGameObject(self.volumeslider)
        self.volumeslider.onValueChanged.addListener(lambda x : JukeBox.setVolume(x[0]))
        self.volumeslider.setActive(False)


        self.volume_img = SpriteTools.getSprite("img/default/volumeIcon.png").img
        self.volume_img_muted = SpriteTools.getSprite("img/default/volumeIcon_Muted.png").img

        self.muteSound = Button((ScreenSize.WidthCenter()+40, ScreenSize.HeightCenter()), self)
        #self.addGameObject(self.muteSound)
        self.muteSound.addSprite(SpriteTools.getSprite("img/default/volumeIcon.png", self))
        self.muteSound.setScale(0.6)
        self.muteSound.onClick.addListener(lambda : self.toggleMute())
        self.addGameObject(self.muteSound)
        self.muteSound.setActive(False)

        self.exitgame = Button((ScreenSize.WidthCenter()-40, ScreenSize.HeightCenter()), self)
        #self.addGameObject(self.exitgame)
        self.exitgame.addSprite(SpriteTools.getSprite("img/default/quitIcon.png", self))
        self.exitgame.setScale(0.6)
        self.exitgame.onClick.addListener(lambda : self.quitGame())
        self.addGameObject(self.exitgame)
        self.exitgame.setActive(False)





    def handleEvents(self, events):
        if self._handleEvents:
            for event in events:
                # This defines a keypress listener
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        self.togglePause()

        super().handleEvents(events)



    def update(self):
        #---
        # Overwrite default update() so our gameobjects work while paused:
        #---
        for gameobject in self.gameobjects:
            #a1Debug.Log("is drawing a spriterect in spriterects")
            if gameobject.active:
                gameobject.update()

        if self._handleEvents:
            self.checkHovering()


    def toggleMute(self):
        if JukeBox.muted:
            self.muteSound.replaceSpriteImg(self.volume_img)
            JukeBox.ToggleMute(False)
        else:
            self.muteSound.replaceSpriteImg(self.volume_img_muted)
            JukeBox.ToggleMute(True)

    def togglePause(self):
        if GameObject._paused:
            GameObject.UnpauseGameObjects()
            self.muteSound.setActive(False)
            self.exitgame.setActive(False)
            self.volumeslider.setActive(False)
        else:
            self.pauseTimer = 0
            GameObject.PauseGameObjects()
            self.exitgame.setActive(True)
            self.muteSound.setActive(True)
            self.volumeslider.setActive(True)

    def quitGame(self):
        SceneManager.running = False
