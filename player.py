import pygame
from random import uniform, randint
from Tools.Particle import ParticleManager
from Tools.Cooldown import Cooldown

"""The Player class."""
class Square(pygame.sprite.Sprite):
    def __init__(self, defLoc = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.Surface = pygame.Surface((40,40))
        self.Surface.fill('blue')
        self.Rect = self.Surface.get_rect(center = defLoc)
        self.x = self.Rect.centerx
        self.y = self.Rect.centery
        
        # Player Physics Stuff
        self.Velx = 0.0
        self.Vely = 0.0
        self.Acceleration = 50.0
        self.DashAcceleration = 600.0
        self.WallBumpAcceleration = 0.0
        self.MaxSpeed = 350.0
        self.Friction = 0.95
        
        # Player Stats Stuff
        self.health = 300.0
        self.stamina = 150.0
        self.baseDamage = 35.0
        self.aoeDamage = 20.0
        
        # Player Input Stuff
        self.userInput = {'down': False, 'right': False, 'up': False, 'left': False, 'dash': False}
        
        # Player cooldown stuff
        self.DashCD = Cooldown(2)
        
        # Player Particle Stuff
        self.ParticleManager = ParticleManager()
        self.vel_and_acc = {'xVel': 0, 'xAcc': 0, 'yVel': 0, 'yAcc': 0}
        
        # CharacterInfo is used in the enemies' reactive AI.
        self.CharacterInfo = {'Vel': (self.Velx, self.Vely), 'Loc': (self.x, self.y)}
        
        
        
    def CharacterInfoUpdate(self): 
        self.CharacterInfo = {'Vel': (self.Velx, self.Vely), 'Loc': (self.x, self.y)}
        return self.CharacterInfo
    
    def _ParticleDirectionCheck(self, direction: str):
        if direction == 'up' or direction == 'down':
            if self.userInput['left']:
                self.vel_and_acc['xVel'] = 300
                self.vel_and_acc['xAcc'] = uniform(-1, -5)
            else:
                self.vel_and_acc['xVel'] = uniform(-5.00,5.00)
                if self.vel_and_acc['xVel'] > 0: self.vel_and_acc['xAcc'] = uniform(0.00, -0.30)
                else: self.vel_and_acc['xAcc'] = uniform(0.00, 0.30)
                
            if self.userInput['right']:
                self.vel_and_acc['xVel'] = -300
                self.vel_and_acc['xAcc'] = uniform(1, 5)
            else:
                self.vel_and_acc['xVel'] = uniform(-5.00,5.00)
                if self.vel_and_acc['xVel'] > 0: self.vel_and_acc['xAcc'] = uniform(0.00, -0.30)
                else: self.vel_and_acc['xAcc'] = uniform(0.00, 0.30)
                
        elif direction == 'left' or direction == 'right':
            if self.userInput['up']:
                self.vel_and_acc['yVel'] = 300
                self.vel_and_acc['yAcc'] = uniform(-1, -5)
            else:
                self.vel_and_acc['yVel'] = uniform(-5.00,5.00)
                if self.vel_and_acc['yVel'] > 0: self.vel_and_acc['yAcc'] = uniform(0.00, -0.30)
                else: self.vel_and_acc['yAcc'] = uniform(0.00, 0.30)
            if self.userInput['down']:
                self.vel_and_acc['yVel'] = -300
                self.vel_and_acc['yAcc'] = uniform(1, 5)
            else:
                self.vel_and_acc['yVel'] = uniform(-5.00,5.00)
                if self.vel_and_acc['yVel'] > 0: self.vel_and_acc['yAcc'] = uniform(0.00, -0.30)
                else: self.vel_and_acc['yAcc'] = uniform(0.00, 0.30)
    
    def _AddParticles(self, direction: str):
        if direction=='down': 
            self._ParticleDirectionCheck(direction='down')
            for par in range(6): self.ParticleManager.add_particle(self.Rect.centerx + randint(-5, 5),
                                                                        self.Rect.top - randint(0, 5),
                                                                        lifetime=0.4, 
                                                                        velx=self.vel_and_acc.get('xVel'),
                                                                        vely=-105,
                                                                        Accely=uniform(1, 5),
                                                                        Accelx=self.vel_and_acc.get('xAcc'),
                                                                        spreadx=uniform(0, 80),
                                                                        spready=0,
                                                                        noisex=(True, 1, 2),
                                                                        noisey=(False, 0, 1),
                                                                        friction=0.99,
                                                                        isRect=True,
                                                                        color=(200,200,200),
                                                                        width=5,
                                                                        height=5)
        elif direction=='up':
            self._ParticleDirectionCheck(direction='up')
            for par in range(6): self.ParticleManager.add_particle(self.Rect.centerx + randint(-5, 5),
                                                                        self.Rect.bottom - randint(-5, 0),
                                                                        lifetime=0.4, 
                                                                        velx=self.vel_and_acc.get('xVel'),
                                                                        vely=105,
                                                                        Accely=uniform(-1, -5),
                                                                        Accelx=self.vel_and_acc.get('xAcc'),
                                                                        spreadx=uniform(0, 80),
                                                                        spready=0,
                                                                        noisex=(True, 1, 2),
                                                                        noisey=(False, 0, 1),
                                                                        friction=0.99,
                                                                        isRect=True,
                                                                        color=(200,200,200),
                                                                        width=5,
                                                                        height=5)
        elif direction=='left':
            self._ParticleDirectionCheck(direction='left')
            for par in range(6): self.ParticleManager.add_particle(self.Rect.right + randint(0, 5),
                                                                        self.Rect.centery - randint(-5, 5),
                                                                        lifetime=0.4,
                                                                        Accelx=uniform(-1, -5),
                                                                        Accely=self.vel_and_acc.get('yAcc'),
                                                                        vely=self.vel_and_acc.get('yVel'),
                                                                        velx=105,
                                                                        spreadx=0,
                                                                        spready=uniform(0, 80),
                                                                        noisex=(False, 0, 1),
                                                                        noisey=(True, 1, 2),
                                                                        friction=0.99,
                                                                        isRect=True,
                                                                        color=(200,200,200),
                                                                        width=5,
                                                                        height=5)
        elif direction=='right':
            self._ParticleDirectionCheck(direction='right')
            for par in range(6): self.ParticleManager.add_particle(self.Rect.left + randint(0, 5),
                                                                        self.Rect.centery - randint(-5, 5),
                                                                        lifetime=0.4,
                                                                        Accelx=uniform(1, 5),
                                                                        Accely=self.vel_and_acc.get('yAcc'),
                                                                        vely=self.vel_and_acc.get('yVel'),
                                                                        velx=-105,
                                                                        spreadx=0,
                                                                        spready=uniform(0, 80),
                                                                        noisex=(False, 0, 1),
                                                                        noisey=(True, 1, 2),
                                                                        friction=0.99,
                                                                        isRect=True,
                                                                        color=(200,200,200),
                                                                        width=5,
                                                                        height=5)
        
    """Checks for wall collision and applies collision-bounce."""
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
    
    """Updates main/basic player movement from user input. Other functions that also update player movement in some way are (most likely) at the end of this function."""
    def updateMovement(self, userInput: dict, dT: float):
        self.userInput = userInput
        
        
        if userInput['down']:
            if self.Vely < self.MaxSpeed:
                self.Vely += self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self._AddParticles('down')
                self.Vely += self.DashAcceleration
                
                
        if userInput['up']:
            if self.Vely > -self.MaxSpeed:
                self.Vely -= self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:  
                self.DashCD.startCD()
                self._AddParticles('up')
                self.Vely -= self.DashAcceleration
                
                
        if userInput['right']:
            if self.Velx < self.MaxSpeed:
                self.Velx += self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self._AddParticles('right')
                self.Velx += self.DashAcceleration
                
                
        if userInput['left']:
            if self.Velx > -self.MaxSpeed:
                self.Velx -= self.Acceleration
            if userInput['dash'] and self.DashCD.checkCD() == False:
                self.DashCD.startCD()
                self._AddParticles('left')
                self.Velx -= self.DashAcceleration
                
                
        self.x += self.Velx * dT
        self.y += self.Vely * dT
        self.Rect.center = (self.x, self.y)
        self.Velx *= self.Friction
        self.Vely *= self.Friction
        
        
    def update(self, userInput: dict, dT: float, WallRects: list = []):
        self.updateMovement(userInput, dT)
        self.updateAbilities(userInput, dT)
        self.WallCollision(WallRects=WallRects)
        self.ParticleManager.update(dT)
        self.CharacterInfoUpdate()
    
    """Draws player to screen"""
    def draw(self, screen):
        pygame.Surface.blit(screen, self.Surface, self.Rect)
        self.ParticleManager.draw(screen)
        
loc = (1920 / 2, 1080 / 2)
player = Square(defLoc=loc)