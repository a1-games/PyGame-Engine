import gameinfo

class ScreenSize():

    @staticmethod
    def Size():
        return gameinfo.aspect_ratio
    
    @staticmethod
    def Center():
        return (ScreenSize.Size()[0] / 2, ScreenSize.Size()[1] / 2)

    @staticmethod
    def Height():
        return ScreenSize.Size()[1]
    
    @staticmethod
    def Width():
        return ScreenSize.Size()[0]

    @staticmethod
    def HeightCenter():
        return ScreenSize.Size()[1] / 2
    
    @staticmethod
    def WidthCenter():
        return ScreenSize.Size()[0] / 2

    @staticmethod
    def Center_OffH(heightDifference):
        return (ScreenSize.Center()[0], ScreenSize.Center()[1] + heightDifference)
    
    @staticmethod
    def Center_OffW(widthDifference):
        return (ScreenSize.Center()[0] + widthDifference, ScreenSize.Center()[1])