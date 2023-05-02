from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.Scene import Scene
from a1.a1Events import a1Event



class Button(GameObject):

    def __init__(self, startpos, scene : Scene, name="noname", alignment=Alignment.Center):
        super().__init__(startpos, name, alignment)
        self.onClick = a1Event()
        self.onPointerEnter = a1Event()
        self.onPointerExit = a1Event()
        self.containsPointer = False
        scene.addButton(self)

    
    def onDestroy(self):
        super().onDestroy()
        Scene.removeButton(self)
 
    def checkContainsPointer(self, mousepos):
        # If we did not contain the cursor last frame:
        if self.containsPointer == False:
            # If we contain the cursor this frame:
            if self.pointIsColliding(mousepos):
                self.containsPointer = True
                self.onPointerEnter.invoke()
                #print("entered")
                return
        # If we did contain the cursor last frame:
        else:
            # If we still contain the cursor:
            if self.pointIsColliding(mousepos):
                return
            # If we no longer contain the cursor:
            else:
                self.containsPointer = False
                self.onPointerExit.invoke()
                #print("exited")



