import pygame
from a1.a1Debug import a1Debug
import sys
from a1.SpriteTools import resource_path

class Sound:
    def __init__(self, sound : pygame.mixer.Sound):
        self.volume = 1
        self.sound = sound

class JukeBox():

    muted = False
    volume = 1

    sounds = {}
    
    @staticmethod
    def setVolume(vol : float):
        if vol == JukeBox.volume:
            # don't overwrite if there is no change
            return
        JukeBox.volume = vol
        pygame.mixer.music.set_volume(vol)

        for soundname in JukeBox.sounds:
            snd = JukeBox.sounds[soundname]
            snd.sound.set_volume(snd.volume * vol)
        #a1Debug.Log("Volume: {}".format(vol))


    @staticmethod
    def loadSound(soundname : str, relativeFilePath : str):
        if ".wav" in relativeFilePath or ".mp3" in relativeFilePath:
            a1Debug.LogWarning("'.mp3' files are not accepted by pygbag. '.wav' may also be denied. Try to use '.ogg' if you want your game to be played in a web browser.")
        JukeBox.sounds[soundname] = Sound(pygame.mixer.Sound(resource_path(relativeFilePath)))

    @staticmethod
    def ToggleMute(muted = True):
        JukeBox.muted = muted
        if muted:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()


    @staticmethod
    def playSound(soundname : str, volume : float = 1.0, looping : bool = False):
        if (JukeBox.muted):
            return
        sound = JukeBox.sounds[soundname]
        sound.sound.set_volume(JukeBox.volume * volume)
        sound.volume = volume
        if looping:
            sound.sound.play(-1)
        else:
            sound.sound.play()
