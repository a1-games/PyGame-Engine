import queue
import asyncio
import pygame
from a1.a1Time import a1Time
from a1.a1Enums import SceneTransition
from a1.Scene import Scene
from a1.TransitionManager import TransitionManager


class SceneManager():
    addingQueue = queue.Queue()
    removalQueue = queue.Queue()
    replacingQueue = queue.Queue()
    
    activeScenes = {}
    running = False
    
    

    # Scene replacing without "dictionary changed size during iteration" errors

    # takes tuple: (replaceLayer, withLayer)
    @staticmethod
    def queueSceneReplacement(replaceLayer : str, withLayer : str):
        SceneManager.replacingQueue.put((replaceLayer, withLayer))


    def replaceScene(layernameToReplace : str, scene : Scene, transition : SceneTransition):
        if SceneManager.activeScenes.__contains__(layernameToReplace):
            TransitionManager.startTransition(SceneManager, layernameToReplace, scene, transition)
        else:
            SceneManager.addScene(scene, layernameToReplace)
            print("Tried to replace scene with nonexisting layername. Added the scene instead.")

            
    @staticmethod
    def sceneReplacing():
        while not SceneManager.replacingQueue.empty():
            replacement = SceneManager.replacingQueue.get()
            if SceneManager.activeScenes.__contains__(replacement[1]):
                SceneManager.activeScenes[replacement[0]] = SceneManager.activeScenes[replacement[1]]
                print("Replaced scene: {} with scene: {}".format(SceneManager.activeScenes[replacement[0]], SceneManager.activeScenes[replacement[1]]))
                SceneManager.removeScene(replacement[1])



    # Scene adding without "dictionary changed size during iteration" errors
    @staticmethod
    def addScene(scene, layername : str):
        scene.InitScene()
        print("initiated scene: {}".format(layername))
        SceneManager.queueSceneAdd((scene, layername))
        # scene needs to be initiated here because if it isnt then TransitionManager can't use it and transitions fail

    # takes tuple: scene = (scene, layername)
    @staticmethod
    def queueSceneAdd(scene):
        SceneManager.addingQueue.put(scene)

    @staticmethod
    def sceneAdding():
        while not SceneManager.addingQueue.empty():
            #print("adding a scene")
            scene = SceneManager.addingQueue.get()
            if not SceneManager.activeScenes.__contains__(scene[1]):
                SceneManager.activeScenes[scene[1]] = scene[0]
                print("Adding Scene: {}".format(scene[1]))
                    
            else:
                print("Tried to add scene to existing layername '{}'. Use replaceScene() instead.".format(scene[1]))

    # Scene removal without "dictionary changed size during iteration" errors    
    @staticmethod
    def removeScene(layername):
        if SceneManager.activeScenes.__contains__(layername):
            print("Queueing Scene for Removal: {}".format(layername))
            SceneManager.queueSceneRemoval(layername)
        else:
            print("Tried to remove scene with nonexisting layername {}".format(layername))
            
    # takes string: layername
    @staticmethod
    def queueSceneRemoval(layername):
        SceneManager.removalQueue.put(layername)
        
    @staticmethod
    def wipe():
        for scenename in SceneManager.activeScenes:
            SceneManager.removeScene(scenename)

    @staticmethod
    def sceneCleanUp():
        while not SceneManager.removalQueue.empty():
            #print("removal queue is not empty")
            layername = SceneManager.removalQueue.get()
            if (SceneManager.activeScenes.__contains__(layername)):
                SceneManager.activeScenes.pop(layername)
                print("removed scene: {}".format(layername))

            
    # Runs the whole game
    @staticmethod
    async def Run(screen):
        if SceneManager.running:
            print("Tried to call SceneManager.Run() while already running!!")
            return

        SceneManager.running = True

        while SceneManager.running:
            
            a1Time.Tick()

            # remove unwanted scenes before iterating through them
            SceneManager.sceneCleanUp()

            # add missing scenes
            SceneManager.sceneAdding()

            # replacing scenes
            SceneManager.sceneReplacing()
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    SceneManager.running = False

            if TransitionManager.transitioning:
                TransitionManager._animateTransition(SceneManager)
                
            # iterate through scenes
            for sceneName in SceneManager.activeScenes:
                #print(sceneName)
                sceneIsActive = SceneManager.activeScenes[sceneName]._active
                if sceneIsActive:
                    # only handle events if the scene is active (dont read key presses during transitions)
                    if not TransitionManager.transitioning:
                        SceneManager.activeScenes[sceneName].handleEvents(events)
                    SceneManager.activeScenes[sceneName].update(pygame.mouse.get_pos())
                    SceneManager.activeScenes[sceneName].draw(screen)
            
            SceneManager.sceneCleanUp()

            # write to screen
            pygame.display.update()

            # webgame necessity
            await asyncio.sleep(0)