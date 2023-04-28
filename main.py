from a1.SceneManager import SceneManager
from a1.ScreenSize import ScreenSize
from a1.a1Time import a1Time
import pygame
import asyncio
import gameinfo

#Import starting scenes:
from Scenes.DebugScene import DebugScene
from Scenes.EmptyScene import EmptyScene
from Scenes.MainScene import MainScene


def main():

    a1Time.ManualInit()

    pygame.init()

    # --- set Game Icon here ---
    pygame_icon = pygame.image.load(gameinfo.game_icon_path)

    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption(gameinfo.game_title)

    screen = pygame.display.set_mode(ScreenSize.Size())
    

    # Add all the layers you need to be able to switch out here:
    SceneManager.addScene(EmptyScene(), "BackgroundLayer")
    SceneManager.addScene(MainScene(), "MainLayer")
    SceneManager.addScene(EmptyScene(), "UILayer")

    # Comment this out if you want (If not, keep it on top):
    SceneManager.addScene(DebugScene(), "FPS Counter")

    # This starts the while loop that runs the game
    # We use asyncio so that it is easy to convert to a webgame / exe build if you need to.
    asyncio.run( SceneManager.Run(screen) )

    pygame.quit()



# call main() on initialization
if __name__ == "__main__":
    main()
    



