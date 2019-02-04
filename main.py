import pygame
pygame.init()
from Classes.Menu import *
from Classes.Projectile import *

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


fond =pygame.image.load("img/fond_jeux.png").convert()
fond = pygame.transform.scale(fond,(Display_Width,Display_Height))
FPS = 60
prolist =[]
pro = pygame.image.load("img/missile.png").convert_alpha()

pro = pygame.transform.scale(pro,(20,40))

Menu_Base()