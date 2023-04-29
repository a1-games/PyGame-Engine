from a1.GameObject import GameObject
from a1.a1Enums import Alignment
from a1.Scene import Scene



class Button(GameObject):

    def __init__(self, startpos, scene : Scene, onclick = None, name="noname", alignment=Alignment.Center):
        super().__init__(startpos, name, alignment)
        self.onClick = onclick
        scene.addButton(self)
    
    def onDestroy(self):
        super().onDestroy()
        Scene.removeButton(self)
 




