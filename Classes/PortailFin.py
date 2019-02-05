import pygame
pygame.init()
from Classes.Controleur import *


Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))

portail_fin = pygame.image.load("img/portailfin.png").convert_alpha()
portail_fin = pygame.transform.scale(portail_fin,(128,128))


class Portailfin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = portail_fin.get_rect()
        self.rect.x = Display_Width-128
        self.rect.y = Display_Height-90-24-64
        self.image = portail_fin
