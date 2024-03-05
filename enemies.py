import pygame
from random import uniform

LIST_OF_ENEMIES = []

class Brain:
    def __init__(self):
        self.CharacterInfo = None
    
    def getInfo(self, CharacterInfo: dict, myInfo: dict): 
        self.CharacterInfo = CharacterInfo
        self.myInfo = myInfo
    
    def Think(self):
        self._DetermineMovement()
        self._DetermineMovement()
    
    def _DetermineMovement(self):
        pass
    
    def _DetermineAction(self):
        pass

class Enemy:
    def __init__(self, locx, locy, width, height, color):
        self.Rect = pygame.Rect(locx, locy, width, height)
        self.x = self.Rect.centerx
        self.y = self.Rect.centery
        self.width = width
        self.height = height
        self.color = color
        
        # Enemy Physics Stuff
        self.Velx = 0.0
        self.Vely = 0.0
        self.Acceleration = 35.0
        self.DashAcceleration = 450.0
        self.WallBumpAcceleration = 0.0
        self.MaxSpeed = 250.0
        self.Friction = 0.8
        
        # Enemy Input Stuff
        self.enemyInput = {'down': False, 'right': False, 'up': False, 'left': False}
        
        # Enemy Stats
        self.health = 100.0
        self.stamina = 100.0
        self.baseDamage = 20.0

        # Enemy AI Stuff
        self.brain = Brain()
        self.ACTION_QUEUE = []
        
    def strategize(self, characterInfo: dict):
        myInfo = {'Vel': (self.Velx, self.Vely), 'Loc': (self.x, self.y), 'Health': self.health, 'Stamina': self.stamina}
        self.brain.getInfo(characterInfo, myInfo)
        self.ACTION_QUEUE = self.brain.Think()
    
    def updateMovement(self, dT):
        pass
    
    def updateAbilities(self):
        pass
    
    def WallCollision(self, WallRects):
        self.Top = (self.Rect.centerx, self.Rect.top)
        self.Bottom = (self.Rect.centerx, self.Rect.bottom)
        self.Left = (self.Rect.left, self.Rect.centery)
        self.Right = (self.Rect.right, self.Rect.centery)
        
        for rect in WallRects:
            
            if rect.collidepoint(self.Top[0], self.Top[1]):
                self.Rect.top = rect.bottom
                self.WallBumpAcceleration = self.Vely * -uniform(2.00, 2.51)
                self.Vely = 0.0
                self.Vely += self.WallBumpAcceleration
            
            elif rect.collidepoint(self.Bottom[0], self.Bottom[1]):
                self.Rect.bottom = rect.top
                self.WallBumpAcceleration = self.Vely * -uniform(2.00, 2.51)
                self.Vely = 0.0
                self.Vely += self.WallBumpAcceleration
            
            elif rect.collidepoint(self.Left[0], self.Left[1]):
                self.Rect.left = rect.right
                self.WallBumpAcceleration = self.Velx * -uniform(2.00, 2.51)
                self.Velx = 0.0
                self.Velx += self.WallBumpAcceleration
                
            elif rect.collidepoint(self.Right[0], self.Right[1]):
                self.Rect.right = rect.left
                self.WallBumpAcceleration = self.Velx * -uniform(2.00, 2.51)
                self.Velx = 0.0
                self.Velx += self.WallBumpAcceleration
    
    def update(self, characterInfo: dict, dT: float, WallRects: list):
        self.strategize(characterInfo=characterInfo)
        self.updateMovement(dT)
        self.WallCollision(WallRects=WallRects)
    
    def draw(self, screen): pygame.draw.circle(screen, self.color, self.Rect.center, self.width * 0.75)