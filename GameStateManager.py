import pygame

class GameStateManager:
    def __init__(self, currentState):
        self.GameStates = None
        self.CurrentState = currentState
        
    def setState(self, state):
        pass
    
    def getState(self):
        return self.CurrentState