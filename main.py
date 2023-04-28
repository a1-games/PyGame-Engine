from a1.SceneManager import SceneManager
from a1.ScreenSize import ScreenSize
from a1.a1Time import a1Time
import pygame
import asyncio
import gameinfo

#Import starting scenes:
from Scenes.BackgroundScene import BackgroundScene
from Scenes.MainScene import MainScene
from Scenes.EmptyScene import EmptyScene
from Scenes.DebugScene import DebugScene

def initGameInfo():
    pygame_icon = pygame.image.load(gameinfo.game_icon_path)
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption(gameinfo.game_title)


def main():

    a1Time.ManualInit()

    pygame.init()

    initGameInfo()
    

    # Add all the layers you need to be able to switch out here:
    # If you need to switch a layer in between others later on, you need to define the layer with an empty scene, as so:
    # SceneManager.addScene(EmptyScene(), "ExampleLayer")

    SceneManager.addScene(BackgroundScene(), "BackgroundLayer")
    SceneManager.addScene(MainScene(), "MainLayer")
    SceneManager.addScene(EmptyScene(), "UILayer")

    # Comment this out if you want (If not, keep it on top):
    SceneManager.addScene(DebugScene(), "FPS Counter")

    # This starts the while loop that runs the game
    # We use asyncio so that it is easy to convert to a webgame / exe build if you need to.
    screen = pygame.display.set_mode(ScreenSize.Size())
    asyncio.run( SceneManager.Run(screen) )

    pygame.quit()



# call main() on initialization
if __name__ == "__main__":
    main()
    



