import pygame

"""Manages gamestates"""
class GameStateManager:
    def __init__(self, currentState):
        self.GameStates = None
        self.CurrentState = currentState
    
    """Sets active game state."""
    def setState(self, state):
        pass
    
    """Returns active game state."""
    def getState(self):
        return self.CurrentState