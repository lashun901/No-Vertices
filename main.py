import pygame, sys
from GameStateManager import GameStateManager
from time import time
from display import screen
from player import player

""" 'GR' refers to 'Global References' """
GR = {
    'screen': screen.screen,
    'player': player
}


_GameStateManager = GameStateManager('main')
userInput = {'down': False, 'right': False, 'up': False, 'left': False, 'dash': False}
clock = pygame.time.Clock()
prevTime = time()
while True:
    dT = time() - prevTime
    prevTime = time()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s:
                userInput['down'] = True
            if e.key == pygame.K_d:
                userInput['right'] = True
            if e.key == pygame.K_w:
                userInput['up'] = True
            if e.key == pygame.K_a:
                userInput['left'] = True
            if e.key == pygame.K_SPACE:
                userInput['dash'] = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_s:
                userInput['down'] = False
            if e.key == pygame.K_d:
                userInput['right'] = False
            if e.key == pygame.K_w:
                userInput['up'] = False
            if e.key == pygame.K_a:
                userInput['left'] = False
            if e.key == pygame.K_SPACE:
                userInput['dash'] = False
    
    screen.update()
    player.update(userInput, dT)
    
    player.draw(GR['screen'])
    pygame.display.flip()
    