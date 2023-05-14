import pygame


class JukeBox():

    muted = False
    volume = 0.2

    musicChannel = None
    effectsChannel = None

    sounds = {}
    
    @staticmethod
    def setVolume(vol : float):
        JukeBox.volume = vol
        pygame.mixer.music.set_volume(vol * 0.5)

    @staticmethod
    def loadSound(soundname : str, filepath : str):
        JukeBox.sounds[soundname] = pygame.mixer.Sound(filepath)

    @staticmethod
    def ToggleMute(muted = True):
        JukeBox.muted = muted
        if muted:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()

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
    def playSound(soundname : str, volume : float = 1.0, looping : bool = False):
        if (JukeBox.muted):
            return
        sound = JukeBox.sounds[soundname]
        sound.set_volume(JukeBox.volume * volume)
        if looping:
            sound.play(-1)
        else:
            sound.play()
