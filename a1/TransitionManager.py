from a1.a1Enums import SceneTransition
from a1.a1Debug import a1Debug
from a1.ScreenSize import ScreenSize
from a1.Scene import Scene
from a1.a1Time import a1Time
import queue


class SceneReplacementObject():
    def __init__(self, nameToReplace : str, replacementScene : Scene, transition : SceneTransition):
        self.nametoreplace = nameToReplace
        self.scene = replacementScene
        self.transition = transition
        self.tmpname = "replacing-{}".format(nameToReplace)
        self.finished = False

class TransitionManager():
    
    # transition
    transitionAddQueue = queue.Queue()
    transitionRemovalQueue = queue.Queue()
    # duration in seconds
    _transSpeed = 0.6
    transDistance = 0
    # duration in seconds
    _fadeSpeed = 0.6

    transitioning = False
    sceneReplacementObjects = []
    
    # error helping
    replacesThisFrame = []

    

    # Scene transitioning without "dictionary changed size during iteration" errors
    def queueTransitionObject(rpo):
        TransitionManager.transitionAddQueue.put(rpo)

    def queueTransitionObjectRemoval(rpo):
        TransitionManager.transitionRemovalQueue.put(rpo)
        
    @staticmethod
    def manageTransitionObjects():
        
        while not TransitionManager.transitionAddQueue.empty():
            #a1Debug.Log("transition adding queue is not empty")
            obj = TransitionManager.transitionAddQueue.get()
            TransitionManager.sceneReplacementObjects.append(obj)
            

        while not TransitionManager.transitionRemovalQueue.empty():
            #a1Debug.Log("transition removal queue is not empty")
            obj = TransitionManager.transitionRemovalQueue.get()
            TransitionManager.sceneReplacementObjects.remove(obj)
            
            if (len(TransitionManager.sceneReplacementObjects) == 0):
                a1Debug.Log("disabling transitions")
                TransitionManager.transitioning = False


        # replacesThisFrame should always be reset after a replacement
        if len(TransitionManager.replacesThisFrame) != 0:
            TransitionManager.replacesThisFrame.clear()
    



    def _animateTransition(SceneManager):

        #a1Debug.Log("--- is animating transition")

        TransitionManager.manageTransitionObjects()

        for rpo in TransitionManager.sceneReplacementObjects:
            
            if rpo.finished == True:
                continue
            
            if rpo.tmpname not in SceneManager.activeScenes:
                a1Debug.LogError("ERROR-TRANSITION: Trying to transition with non-existent scene.")
                TransitionManager._endTransition(rpo, SceneManager)
                continue
            
            transspeed = a1Time.DeltaTime / TransitionManager._transSpeed * TransitionManager.transDistance
            fadespeed = a1Time.DeltaTime / TransitionManager._fadeSpeed

            fromPos = SceneManager.activeScenes[rpo.nametoreplace].position
            toPos = SceneManager.activeScenes[rpo.tmpname].position

            toDist = (0, 0)
            fromDist = (0, 0)

            #a1Debug.Log("_animateTransition")

            if rpo.transition == SceneTransition.CrossFade:
                toOpacity = SceneManager.activeScenes[rpo.tmpname].opacity
                fromOpacity = SceneManager.activeScenes[rpo.nametoreplace].opacity

                SceneManager.activeScenes[rpo.tmpname].setOpacity(toOpacity + fadespeed)
                SceneManager.activeScenes[rpo.nametoreplace].setOpacity(fromOpacity - fadespeed)
                # when done:
                if SceneManager.activeScenes[rpo.tmpname].opacity >= 1:
                    #a1Debug.Log("---opacity transition ended: {}".format(SceneManager.activeScenes[rpo.tmpname].opacity))
                    SceneManager.activeScenes[rpo.tmpname].opacity = 1
                    TransitionManager._endTransition(rpo, SceneManager)
                    continue

            elif rpo.transition == SceneTransition.Slide_R2L:
                toDist = (toPos[0] - transspeed, toPos[1])
                fromDist = (fromPos[0] - transspeed, fromPos[1])
                # when done:
                if SceneManager.activeScenes[rpo.tmpname].position[0] <= 0:
                    TransitionManager._endTransition(rpo, SceneManager)
                    continue

            elif rpo.transition == SceneTransition.Slide_L2R:
                toDist = (toPos[0] + transspeed, toPos[1])
                fromDist = (fromPos[0] + transspeed, fromPos[1])
                # when done:
                if SceneManager.activeScenes[rpo.tmpname].position[0] >= 0:
                    TransitionManager._endTransition(rpo, SceneManager)
                    continue

            elif rpo.transition == SceneTransition.Slide_T2B:
                toDist = (toPos[0], toPos[1] + transspeed)
                fromDist = (fromPos[0], fromPos[1] + transspeed)
                # when done:
                if SceneManager.activeScenes[rpo.tmpname].position[1] >= 0:
                    TransitionManager._endTransition(rpo, SceneManager)
                    continue

            elif rpo.transition == SceneTransition.Slide_B2T:
                toDist = (toPos[0], toPos[1] - transspeed)
                fromDist = (fromPos[0], fromPos[1] - transspeed)
                # when done:
                if SceneManager.activeScenes[rpo.tmpname].position[1] <= 0:
                    TransitionManager._endTransition(rpo, SceneManager)
                    continue
            
            SceneManager.activeScenes[rpo.tmpname].setPosition(toDist)
            SceneManager.activeScenes[rpo.nametoreplace].setPosition(fromDist)
        


    def _endTransition(rpo : SceneReplacementObject, SceneManager):
        #a1Debug.Log("ending transition")
        rpo.finished = True

        SceneManager.activeScenes[rpo.tmpname].setPosition((0, 0))

        TransitionManager.queueTransitionObjectRemoval(rpo)

        # we can only replace if transitioning == false
        SceneManager.queueSceneReplacement(rpo.nametoreplace, rpo.tmpname)
        pass
    
    

    # Scene replacing without "dictionary changed size during iteration" errors
    # With transitions
    @staticmethod
    def startTransition(SceneManager, scenenameToReplace : str, scene : Scene, transition : SceneTransition):

        rpo = SceneReplacementObject(scenenameToReplace, scene, transition)
        
        # transition speed glitch prevention:
        for name in TransitionManager.replacesThisFrame:
            if name == scenenameToReplace:
                a1Debug.LogWarning("Tried to replace the same scene more than once (This was prevented). \nThis could be because you cause a scene change on multiple button presses in the same frame (?)")
                return
        else:
            TransitionManager.replacesThisFrame.append(scenenameToReplace)

        # if transition is none, instantly replace
        if rpo.transition == SceneTransition._None:
            SceneManager.addScene(rpo.scene, rpo.tmpname)
            SceneManager.queueSceneReplacement(rpo.nametoreplace, rpo.tmpname)
        else: # else, do cool transition
            #a1Debug.Log("transition started")
                
            # replacement is queued at the end of the transition
            SceneManager.addScene(rpo.scene, rpo.tmpname)

            # set invisible
            if rpo.transition == SceneTransition.CrossFade:
                rpo.scene.setOpacity(0)
                #a1Debug.Log("opacity: {}".format(rpo.scene.opacity))

            # set position outside the screen
            elif rpo.transition == SceneTransition.Slide_L2R:
                rpo.scene.position = (-ScreenSize.Width(), 0)
                TransitionManager.transDistance = ScreenSize.Width()

            elif rpo.transition == SceneTransition.Slide_R2L:
                rpo.scene.position = (ScreenSize.Width(), 0)
                TransitionManager.transDistance = ScreenSize.Width()

            elif rpo.transition == SceneTransition.Slide_B2T:
                rpo.scene.position = (0, ScreenSize.Height())
                TransitionManager.transDistance = ScreenSize.Height()

            elif rpo.transition == SceneTransition.Slide_T2B:
                rpo.scene.position = (0, -ScreenSize.Height())
                TransitionManager.transDistance = ScreenSize.Height()
            else:
                pass
                
            TransitionManager.queueTransitionObject(rpo)
            TransitionManager.transitioning = True
    

