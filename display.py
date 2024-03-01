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
# Tilesize is (32, 50).
tilemapBASE = ['BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B....B.BBBBBBBBBBB....BBBBBBBBBB...........................B',
               'B......BBBBBBBBBBB.........................................B',
               'B..........................................................B',
               'B...........................P..............................B',
               'B..........................................................B',
               'B..........................................................B',
               'B....................BBBBBBBBBBB...........................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'B..........................................................B',
               'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB']
        

class Map:
    def __init__(self, screen=screen.screen, TileMap: str = tilemapBASE):
        self.screen = screen
        self.TileMap = TileMap
        
        self.BorderTileSurface = pygame.Surface((tilesize[0],tilesize[1]))
        self.BorderTileSurface.fill('brown')
        self.BorderTileRects = []
    
    def buildMap(self):
        for tileMapY, list_of_tiles in enumerate(self.TileMap):
            for tileMapX, tile in enumerate(list_of_tiles):
                if tile == 'B':
                    self.BorderTileRects.append(self.BorderTileSurface.get_rect(topleft = (tileMapX * tilesize[0], tileMapY * tilesize[1])))
        
        for rect in self.BorderTileRects:
            pygame.Surface.blit(self.screen, self.BorderTileSurface, rect)
        print(f'Rect Number: {self.BorderTileRects[0]}\n')
        self.BorderTileRects = []

myMap = Map()