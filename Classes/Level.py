import pygame
pygame.init()
from Classes.Controleur import *
from Classes.PortailFin import *
from Classes.Platform import *
from Classes.Portable import *
from Classes.Bonus import *

import random

# from Classes.Projectile import *
# from Classes.Lancerocket import *


global level_en_cours_numero

Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))

fond = pygame.image.load("images/background.png").convert()
fond = pygame.transform.scale(fond,(Display_Width,Display_Height))

class Level(object):
    def __init__(self, player):
        self.portal = pygame.sprite.Group()
        self.portal.add(Portailfin())
        self.portables_list = pygame.sprite.Group()
        self.bonus_list = pygame.sprite.Group()
        self.plats = pygame.sprite.Group()
        for i in range(0,8):
            self.plats.add(Platform(i*208-63*(i+1),680))
        self.player = player
        self.background = None

    def draw(self, screen):
        Display.blit(fond,(0,0))
        self.portal.draw(screen)
        self.portables_list.draw(screen)
        self.bonus_list.draw(screen)
        self.plats.draw(screen)

    def show_port(self, level_portables):
        self.portables_list.empty()
        for port in level_portables:
            # Changer 2eme valeur pour taux d'apparition
            rand = random.randint(0, 1)
            if rand == 1: # ajouter/enlever or rand == 0 (pour tests)
                portable = Portable(port[0], port[1])
                self.portables_list.add(portable)

    def show_bonus(self, level_bonus):
        self.bonus_list.empty()
        for bon in level_bonus:
            # Changer 2eme valeur pour taux d'apparition
            rand = random.randint(0, 0)
            if rand == 0: # ajouter/enlever or rand == 0 (pour tests)
                bonus = Bonus(bon[0], bon[1])
                self.bonus_list.add(bonus)

class Level_1(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        # PORTABLES
        self.level_portables = [[50,150],
                                [100,150],
                                [150,150],

                                [300,200],
                                [350,200],

                                [50,300],
                                [100,300],
                                [150,300],

                                [50,450],
                                [100,450],
                                [150,450],
                                [200,450],

                                [200,600],
                                [250,600],
                                [300,600],

                                [550,600],
                                [600,600],
                                [650,600],

                                [550,500],
                                [600,500],
                                [650,500],

                                [950,150],
                                [900,150],
                                [850,150],

                                [950,300],
                                [900,300],
                                [850,300],

                                [650,150],
                                [650,250],
                                [650,350],

                                [900,700],
                                [900,600],
                                [900,500]]

        self.show_port(self.level_portables)

        # BONUS
        self.level_bonus = [[950,400],[300,300],[500,600]]
        self.show_bonus(self.level_bonus)

class Level_2(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.level_portables = []
        #A AJOUTER

class Level_3(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.level_portables = []
        #A AJOUTER

class Level_alea(Level):
    def __init__(self, player):
        Level.__init__(self, player)
#         a = random.randint(0,1200)
#         b = random.randint(0,1200)
#         c = random.randint(0,1200)
#         d = random.randint(0,1200)
#         e = random.randint(0,1200)
#         f = random.randint(0,1200)
#         g = random.randint(0,1200)
#         h = random.randint(0,1200)
#         i = random.randint(0,1200)
#         j = random.randint(0,1200)
#         rand_list = [a,b,c,d,e,f,g,h,i,j]
# ##        for i in rand_list:
# ##            if i == rand_list[-10:]+30 or i == rand_list[-10:]-30:
# ##                i = random.randrange(0,1200)a
#
#         ac=random.randrange(2,12)
#         bc=random.randrange(2,12)
#         cc=random.randrange(2,12)
#         dc=random.randrange(2,12)
#         ec=random.randrange(2,12)
#         fc=random.randrange(2,12)
#         gc=random.randrange(2,12)
#         hc=random.randrange(2,12)
#         ic=random.randrange(2,12)
#         jc=random.randrange(2,12)
#
#
#         level =[[a,ac,a-30],
#                 [b,bc,b-30],
#                 [c,cc,c-30],
#                 [d,dc,d-30],
#                 [e,ec,e-30],
#                 [f,fc,f-30],
#                 [g,gc,g-30],
#                 [h,hc,h-30],
#                 [i,ic,i-30],
#                 [j,jc,j-30],
#
#                             ]

#         for misille in level:
# #            pro = Projectil(misille[0],misille[1])
#             lance = Lance_rocket(misille[2])
# #            self.pro_list.add(pro)
#             self.lance_list.add(lance)
