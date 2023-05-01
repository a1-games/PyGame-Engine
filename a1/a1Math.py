import math

@staticmethod
def Normalize(Vector2):
    #if Vector2[0] > -1 and Vector2[0] < 1 or Vector2[1] > -1 and Vector2[1] < 1:
        #print("WARNING! a1Math.Normalize can't handle values between -1 and 1. Perhaps Multiply by 100 before normalizing?")

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


