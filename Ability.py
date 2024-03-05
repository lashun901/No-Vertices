import pygame


class Ability:
    def __init__(self, name: str, Player: object, CooldownList: list = [float, float, float, float]):
        self.name = name
        self.Cooldowns = CooldownList
        self.PlayerInput = Player.userInput

    def getName(self): return self.name
    
    def getCooldowns(self): return self.Cooldowns
    




class SeismicStomp(Ability):
    def __init__(self, name: str, CooldownList: list = [float, float, float, float], PlayerInput: dict = { str: bool }):
        super().__init__(name, CooldownList, PlayerInput)
    
    