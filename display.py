import pygame
class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Pixel Survival')
    
    def colorScreen(self):
        self.screen.fill('#222222')
    
    def update(self):
        self.colorScreen()  
screen = Display()

tilesize = (32,60)
# 
tilemapBASE = ['BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B......BBBBBBBBBBB....BBBBBBBBBB...........................B',
               'B......BBBBBBBBBBB.........................................B',
               'B..........................................................B',
               'B...........................P..............................B',
               'B..........................................................B',
               'B..........................................................B',
               'B....................BBBBBBBBBBB............................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB']

class Tilemap:
    def __init__(self, TilemapStr: str = None):
        self.tilemap = TilemapStr
        

class Map:
    def __init__(self, TileMap: str = None):
        self.TileMap = TileMap
        
    
    