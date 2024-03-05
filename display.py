import pygame

WindowSize = (1920, 1080)
"""Creates a Pygame 'display'."""
class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode(WindowSize)
        pygame.display.set_caption('Pixel Survival')
    
    """Gives window background color."""
    def colorScreen(self):
        self.screen.fill('#222222')
    
    """Updates window."""
    def update(self):
        self.colorScreen()  
screen = Display()

tilesize = (32,60)

"""A basic tilemap."""
tilemapBASE = ['BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
               'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BB........................................................BB',
               'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
               'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB']

"""Map class is used to create, update, and manage tiles used on the tilemap."""
class Map:
    def __init__(self, screen = screen.screen, TileMap: str = tilemapBASE):
        self.TileMap = TileMap
        self.screen = screen
        
        self.BorderSurface = pygame.Surface((tilesize[0], tilesize[1]))
        self.BorderRects = []
        
        self.WallSurface = pygame.Surface((tilesize[0], tilesize[1]))
        self.WallSurface.fill('#17131a')
        self.WallRects = []
        
        self.TileRects = []
        
        self.PlayerLoc = None

    """Creates and updates map from supplied TileMap."""
    def buildMap(self):
        self.TileRects = []
        self.BorderRects = []
        self.WallRects = []
        for ValueY, list_of_tiles in enumerate(self.TileMap):
            for ValueX, tile in enumerate(list_of_tiles):
                if tile == 'B': self.BorderRects.append(self.BorderSurface.get_rect(topleft = (tilesize[0] * ValueX, tilesize[1] * ValueY)))
                elif tile == 'W': self.WallRects.append(self.WallSurface.get_rect(topleft = (tilesize[0] * ValueX, tilesize[1] * ValueY)))
                elif tile == 'P': self.PlayerLoc = (tilesize[0] * ValueX, tilesize[1] * ValueY)
        self.TileRects = self.BorderRects + self.WallRects
        
        for rect in self.BorderRects: pygame.Surface.blit(self.screen, self.BorderSurface, rect)
        for rect in self.WallRects: pygame.Surface.blit(self.screen, self.WallSurface, rect)
        
        
        
mapp = Map()