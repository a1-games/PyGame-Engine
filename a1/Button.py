from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.Scene import Scene



class Button(GameObject):

    containsPointer = False

    def __init__(self, startpos, scene : Scene, onclick = None, name="noname", alignment=Alignment.Center):
        super().__init__(startpos, name, alignment)
        scene.addButton(self)

        self.onClick = onclick
        self.onPointerEnter = None
        self.onPointerExit = None
    
    def onDestroy(self):
        super().onDestroy()
        Scene.removeButton(self)
 
    def checkContainsPointer(self, mousepos):
        # If we did not contain the cursor last frame:
        if self.containsPointer == False:
            # If we contain the cursor this frame:
            if self.pointIsColliding(mousepos):
                self.containsPointer = True
                self.onPointerEnter()
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
                self.onPointerExit()
                #print("exited")



