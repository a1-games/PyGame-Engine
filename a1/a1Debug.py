# https://www.geeksforgeeks.org/print-colors-python-terminal/

class a1Debug:

    Enabled = True

    @staticmethod
    def Log(msg : str):
        if a1Debug.Enabled:
            print(msg)
            

    @staticmethod
    def LogWarning(msg : str):
        if a1Debug.Enabled:
            print("\033[93mWarning: {}\033[00m".format(msg))
            

    @staticmethod
    def LogError(msg : str):
        if a1Debug.Enabled:
            print("\033[91mError: {}\033[00m".format(msg))
            
            