import enum

class Alignment(enum.Enum):
    Center = 0,
    TopLeft = 1,
    TopRight = 2,
    BottomLeft = 3,
    BottomRight = 4,
    TopMiddle = 5,
    BottomMiddle = 6
    LeftMiddle = 7,
    RightMiddle = 8,

    
class SceneTransition(enum.Enum):
    _None = 0,
    Slide_R2L = 1,
    Slide_L2R = 2,
    Slide_T2B = 3,
    Slide_B2T = 4,
    CrossFade = 5,

    
class SpriteDirection(enum.Enum):
    _None = 0,
    North = 1,
    East = 2,
    South = 3,
    West = 4,

