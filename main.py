import pygame, sys
from GameStateManager import GameStateManager
from time import time
from display import screen, mapp
from player import player
from enemies import *

""" 'GR' refers to 'Global References' """
GR = {
    'screen': screen.screen,
    'player': player,
    'enemy list': LIST_OF_ENEMIES
}


_GameStateManager = GameStateManager('main')
userInput = {'down': False, 'right': False, 'up': False, 'left': False, 'dash': False, 'q': False}
clock = pygame.time.Clock()
prevTime = time()
while True:
    """For loop is the Event loop for No Vertices."""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s: userInput['down'] = True
            if e.key == pygame.K_d: userInput['right'] = True
            if e.key == pygame.K_w: userInput['up'] = True
            if e.key == pygame.K_a: userInput['left'] = True
            if e.key == pygame.K_SPACE: userInput['dash'] = True
            if e.key == pygame.K_q: userInput['q'] = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_s: userInput['down'] = False
            if e.key == pygame.K_d: userInput['right'] = False
            if e.key == pygame.K_w: userInput['up'] = False
            if e.key == pygame.K_a: userInput['left'] = False
            if e.key == pygame.K_SPACE: userInput['dash'] = False
            if e.key == pygame.K_q: userInput['q'] = False
    
    # dT is used in Physics calculations.
    dT = time() - prevTime
    prevTime = time()
    
    screen.update()
    mapp.buildMap()
    
    player.update(userInput, dT, mapp.TileRects)
    for index, enemy in (GR['enemy list']):
        if enemy.isDead(): GR['enemy list'].pop(index)
        else: 
            enemy.update(player.userInfo, dT, mapp.TileRects)
            enemy.draw(GR['screen'])
    
    player.draw(GR['screen'])
    
    # Displays window.
    pygame.display.flip()
    