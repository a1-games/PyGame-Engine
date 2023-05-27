# https://www.geeksforgeeks.org/print-colors-python-terminal/
from a1.ConsoleColors import ConsoleColors

class a1Debug:

    Enabled = True

    @staticmethod
    def Log(msg : str):
        if a1Debug.Enabled:
            print(str(msg))
            

    @staticmethod
    def LogWarning(msg : str):
        if a1Debug.Enabled:
            print("{}Warning: {}{}".format(ConsoleColors.t_red, str(msg), ConsoleColors.reset))
            

    @staticmethod
    def LogError(msg : str):
        if a1Debug.Enabled:
            print("{}Error: {}{}".format(ConsoleColors.t_yellow, str(msg), ConsoleColors.reset))


    # just for funsies 
    @staticmethod
    def LogRainbow(msg : str):
        if a1Debug.Enabled:
            rnbwMsg = ConsoleColors.bold
            colorIndex = 0
            for char in str(msg):
                rnbwMsg += "{}{}".format(ConsoleColors.rainbowRange[colorIndex], char)
                colorIndex += 1
                if colorIndex >= len(ConsoleColors.rainbowRange):
                    colorIndex = 0
            rnbwMsg += ConsoleColors.reset
            print(rnbwMsg)
            
    @staticmethod
    def LogPoliceTape(msg : str):
        if a1Debug.Enabled:
            # idk why it wont let me do bold coloured text on a coloured background. perhaps only 2 styles per print??
            tapeMsg = ConsoleColors.bg_yellow + ConsoleColors.bold + ConsoleColors.t_black + " " + msg + " " + ConsoleColors.reset
            print(tapeMsg)





            