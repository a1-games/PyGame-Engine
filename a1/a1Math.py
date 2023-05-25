import math


@staticmethod
def pythag(a, b):
    a2 = math.pow(a, 2)
    b2 = math.pow(b, 2)
    return math.sqrt(a2 + b2)

@staticmethod
def Normalize(Vector2):
    #if Vector2[0] > -1 and Vector2[0] < 1 or Vector2[1] > -1 and Vector2[1] < 1:
        #a1Debug.Log("WARNING! a1Math.Normalize can't handle values between -1 and 1. Perhaps Multiply by 100 before normalizing?")

    x = Vector2[0]
    y = Vector2[1]

    # use pythagoras to finx the length of the hypotenuse
    x2 = math.pow(x, 2)
    y2 = math.pow(y, 2)
    pythag = math.sqrt(x2 + y2)
    
    # divide the vector by the length of the hypotenuse
    normX = x / pythag
    normY = y / pythag

    # return normalize x and y as tuple vector
    return (normX, normY)


@staticmethod
def VectorDistance(vec1, vec2):

    # use pythagoras to finx the length of the hypotenuse
    x2 = math.pow(vec1[0] - vec2[0], 2)
    y2 = math.pow(vec1[1] - vec2[1], 2)
    pythag =  math.sqrt(x2 + y2)
    
    # by calculating the vector before the magnitude, we ensure that the magnitude is never < 0
    return math.sqrt(x2 + y2)