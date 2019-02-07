import pygame
pygame.init()
from Classes.Controleur import *
from Classes.PortailFin import *
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
        self.pro_list = pygame.sprite.Group()
        self.lance_list = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.portal.add(Portailfin())
        self.portables_list = pygame.sprite.Group()
        self.bonus_list = pygame.sprite.Group()
        self.player = player
        self.background = None

    def update(self):
        for i in self.pro_list:
            i.Fall()
        self.pro_list.update()
        self.lance_list.update()

    def draw(self, screen):
        Display.blit(fond,(0,0))
        self.pro_list.draw(screen)
        self.lance_list.draw(screen)
        self.portal.draw(screen)
        self.portables_list.draw(screen)
        self.bonus_list.draw(screen)

    def show_port(self, level_portables):
        self.portables_list.empty()
        for port in level_portables:
            rand = random.randint(0, 1)
            if rand == 1:
                portable = Portable(port[0], port[1])
                self.portables_list.add(portable)

class Level_1(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.level_portables = [[40,140],
                                [80,140],
                                [120,140],

                                [40,250],
                                [120,250],

                                [140,200],
                                [180,200],
                                [220,200],

                                [40,400],
                                [60,400],
                                [80,400],
                                [100,400],
                                ]

        self.show_port(self.level_portables)

        #if affichBonus :
        level_bonus = [[400,400],[300,300]]

        for port in level_bonus :
            bonus = Bonus(port[0],port[1])
            self.bonus_list.add(bonus)

class Level_2(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        #A AJOUTER

class Level_3(Level):
    def __init__(self, player):
        Level.__init__(self, player)
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
