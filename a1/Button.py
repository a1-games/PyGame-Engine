from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.a1Events import a1Event
from a1.a1Debug import a1Debug



class Button(GameObject):

    def __init__(self, startpos, scene, name="noname", spritealignment=Alignment.Center, textalignment=None, textIsRelative : bool = False):
        super().__init__(startpos, name, spritealignment, textalignment, textIsRelative)
        self.onClick = a1Event()
        self.isDown = False
        self.onRelease = a1Event()
        self.onPointerEnter = a1Event()
        self.onPointerExit = a1Event()
        self.containsPointer = False
        scene.addButton(self)
 

    def checkPointerExit(self, mousepos):
        # If we did contain the cursor last frame:
        if self.containsPointer:
            # If we still contain the cursor:
            if self.pointIsColliding(mousepos):
                return
            # If we no longer contain the cursor:
            else:
                self.containsPointer = False
                self.onPointerExit.invoke()
                #a1Debug.Log("exited")

    def checkPointerEnter(self, mousepos):
        # If we did not contain the cursor last frame:
        if self.containsPointer == False:
            # If we contain the cursor this frame:
            if self.pointIsColliding(mousepos):
                self.containsPointer = True
                self.onPointerEnter.invoke()
                #a1Debug.Log("entered")
                return




