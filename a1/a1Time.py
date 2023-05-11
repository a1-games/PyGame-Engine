#import pygame
import time

class a1Time():
    
    _paused = False

    _startTime = 0.0
    _lastFrame = 0.0
    _frameCount = 0.0
    _nextFpsCheck = 0.0
    _timeBetweenFpsChecks = 0.4

    Fps = 0.0
    DeltaTime = 0.0
    NowTime = 0.0

    @staticmethod
    def PauseDelta():
        a1Time._paused = True

    @staticmethod
    def UnpauseDelta():
        a1Time._paused = False

    @staticmethod
    def ManualInit():
        a1Time._startTime = time.time()
        #a1Time._lastFrame = pygame.time.get_ticks()
        
        
    @staticmethod
    def Tick():
        # Time
        a1Time.NowTime = time.time() - a1Time._startTime
        #print(nowTime)

        # deltaTime
        a1Time.DeltaTime = a1Time.NowTime - a1Time._lastFrame
        a1Time._lastFrame = a1Time.NowTime
        if a1Time._paused:
            a1Time.DeltaTime = 0

        # fps counter
        a1Time._frameCount += 1
        if (a1Time.NowTime >= a1Time._nextFpsCheck):
            a1Time.Fps = int(a1Time._frameCount / a1Time._timeBetweenFpsChecks)
            a1Time._nextFpsCheck = a1Time.NowTime + a1Time._timeBetweenFpsChecks
            a1Time._frameCount = 0





