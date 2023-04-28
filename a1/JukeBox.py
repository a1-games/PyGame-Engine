import pygame


class JukeBox():

    muted = False
    volume = 0.2

    musicChannel = None
    effectsChannel = None
    
    def setVolume(vol : float):
        JukeBox.volume = vol
        pygame.mixer.music.set_volume(vol * 0.5)

    def ManualInit(self):
        JukeBox.pewSound = pygame.mixer.Sound("sound/pew.wav")
        JukeBox.explSound = pygame.mixer.Sound("sound/explosion.wav")

    def ToggleMute(muted = True):
        JukeBox.muted = muted
        if muted:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()

    @staticmethod
    def playSound(filePath, looping : bool = False):
        if (JukeBox.muted):
            return
        sound = pygame.mixer.Sound(filePath)
        sound.set_volume(JukeBox.volume)
        if looping:
            sound.play(-1)
        else:
            sound.play()

    @staticmethod
    def playMusic(filePath, looping : bool = False):
        if (JukeBox.muted):
            return
        sound = pygame.mixer.Sound(filePath)
        sound.set_volume(JukeBox.volume * 0.3)
        if looping:
            sound.play(-1)
        else:
            sound.play()

    @staticmethod
    def playPewSound():
        if (JukeBox.muted):
            return
        sound = pygame.mixer.Sound(JukeBox.pewSound)
        sound.set_volume(JukeBox.volume * 0.3)
        sound.play()

    @staticmethod
    def playExplosionSound():
        if (JukeBox.muted):
            return
        sound = pygame.mixer.Sound(JukeBox.explSound)
        sound.set_volume(JukeBox.volume)
        sound.play()