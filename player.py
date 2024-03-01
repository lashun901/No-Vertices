import pygame
from time import time
from Tools.Cooldown import Cooldown

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.Surface = pygame.Surface((50,50))
        self.Surface.fill('blue')
        self.Rect = self.Surface.get_rect(center = (x,y))
        self.x = self.Rect.centerx
        self.y = self.Rect.centery
        self.CornerCoordinate = self.Rect.topleft
        
        # Player Physics Stuff
        self.Velx = 0.0
        self.Vely = 0.0
        self.Acceleration = 40.0
        self.DashAcceleration = 2500.0
        self.MaxSpeed = 800.0
        self.Friction = 0.95
        
        # Player Input Stuff
        self.userInput = {'down': False, 'right': False, 'up': False, 'left': False, 'dash': False}
        
        # Player cooldown stuff
        self.DashCD = Cooldown(3)
    
    def update(self, userInput: dict, dT: float):
        if userInput['down']:
            if self.Vely < self.MaxSpeed:
                self.Vely += self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self.Vely += self.DashAcceleration
        if userInput['up']:
            if self.Vely > -self.MaxSpeed:
                self.Vely -= self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self.Vely -= self.DashAcceleration
        if userInput['right']:
            if self.Velx < self.MaxSpeed:
                self.Velx += self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self.Velx += self.DashAcceleration
        if userInput['left']:
            if self.Velx > -self.MaxSpeed:
                self.Velx -= self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self.Velx -= self.DashAcceleration
        self.x += self.Velx * dT
        self.y += self.Vely * dT
        self.Rect.center = (self.x, self.y)
        self.Velx *= self.Friction
        self.Vely *= self.Friction
        
        self.userInput = userInput
        
    def draw(self, screen):
        pygame.Surface.blit(screen, self.Surface, self.Rect)
    
    

x = 1920/2
y = 1080/2

player = Square(x, y)