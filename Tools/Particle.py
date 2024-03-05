import pygame
from random import uniform, choice
from time import time

# Particle class
class Particle:
    def __init__(self, x, y, lifetime, Accelx = 0.0, Accely = 0.0, velx = 0.0, vely = 0.0, spreadx = 0.0, spready = 0.0, noisex = (True, 1, 2), noisey = (True, 1, 2), friction = 0.92, isCirc: bool = False, isRect: bool = False,color: str | tuple = (200, 200, 200), width: int = 8, height: int = 8, borderWidth: int = 8, border_radius: int = 8):
        self.isCirc = isCirc
        self.isRect = isRect
        self.color = color
        self.x = x
        self.y = y
        self.Rect = pygame.Rect(0,0,width,height)
        self.Rect.center = (self.x, self.y)
        self.borderWidth = borderWidth
        self.borderRadius = border_radius
        self.Velx = velx
        self.Vely = vely
        self.noisex = noisex
        self.noisey = noisey
        self.Accelx =Accelx
        self.Accely = Accely
        self.spreadx = spreadx
        self.spready = spready
        self.spread_direction = choice([-1,1])
        self.lifetime = lifetime
        self.epoch = None
        self.kill = False
        self.friction = friction
        
        if self.noisex[0]: self.noisex = uniform(self.noisex[1], self.noisex[2])
        else: self.noisex = 1
        if self.noisey[0]: self.noisey = uniform(self.noisey[1], self.noisey[2])
        else: self.noisey = 1

    def update(self, dT):
        
        if (self.Velx > 0 and self.Accelx < 0) or (self.Velx < 0 and self.Accelx > 0):
            self.Velx += self.Accelx
            self.x += (self.Velx + (self.spread_direction * self.noisex * self.spreadx)) * dT
        self.Velx *= self.friction
            
        if (self.Vely > 0 and self.Accely < 0) or (self.Vely < 0 and self.Accely > 0):
            self.Vely += self.Accely
            self.y += (self.Vely + (self.spread_direction * self.noisey * self.spready)) * dT
        self.Vely *= self.friction
        
        if self.epoch == None: self.epoch = time()
        elif (time() - self.epoch) >= self.lifetime: return True
        else: return False
            

    def draw(self, window):
        position = (int(self.x), int(self.y))
        
        if self.isCirc: pygame.draw.circle(window, self.color, position, 3)
        elif self.isRect:
            self.Rect.center = position
            pygame.draw.rect(window, self.color, self.Rect, self.borderWidth, self.borderRadius)

# Particle system class
class ParticleManager:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y, lifetime, Accelx = 0.0, Accely = 0.0, velx = 0.0, vely = 0.0, spreadx = 0.0, spready = 0.0, noisex = (True, 1, 2), noisey = (True, 1, 2), friction = 0.92, isCirc: bool = False, isRect: bool = False, color: str | tuple = (200, 200, 200), width: int = 8, height: int = 8, borderWidth: int = 8, border_radius: int = 8):
        self.particles.append(Particle(x, y, lifetime, Accelx, Accely, velx, vely, spreadx, spready, noisex, noisey, friction, isCirc, isRect, color, width, height, borderWidth, border_radius))

    def update(self, dT):
        for index, particle in enumerate(self.particles):
            kill = particle.update(dT)
            if kill: self.particles.pop(index)

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)
