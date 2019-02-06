import pygame
pygame.init()
from Classes.Controleur import *

Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))

portable = pygame.image.load("images/portable.png").convert_alpha()
portable = pygame.transform.scale(portable,(30,60))

class Portable(pygame.sprite.Sprite):
    # x location, y location
    def __init__(self,xloc,yloc):
        pygame.sprite.Sprite.__init__(self)
        self.rect = portable.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        self.image = portable
