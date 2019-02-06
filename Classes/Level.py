import pygame
pygame.init()
from Classes.Controleur import *
from Classes.PortailFin import *
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

class Level_1(Level):
    def __init__(self, player):


        Level.__init__(self, player)
        # defini vitesse de chaque lance rocket
        # level =[[100,3,70],
        #         [200,6,170],
        #         [300,4,270],
        #         [400,6,370],
        #         [500,4,470],
        #         [600,6,570],
        #         [700,7,670],
        #         [800,3,770],
        #         [900,5,870],
        #         [1000,4,970],
        #         [1100,6,1070],]

#        for misille in level:
#            projectile = Projectil(misille[0],misille[1])
#            lance = Lance_rocket(misille[2])
#            self.pro_list.add(projectile)
#            self.lance_list.add(lance)


class Level_2(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        # level =[[100,5,70],
        #         [200,10,170],
        #         [300,7,270],
        #         [400,8,370],
        #         [500,9,470],
        #         [600,4,570],
        #         [700,3,670],
        #         [800,9,770],
        #         [900,9,870],
        #         [1000,9,970],
        #         [1100,9,1070],]

#         for misille in level:
#            pro = Projectil(misille[0],misille[1])
#            lance = Lance_rocket(misille[2])
#            self.pro_list.add(pro)
#            self.lance_list.add(lance)

class Level_3(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        # level =[[80,3,80-30],
        #         [150,2,120],
        #         [250,6,220],
        #         [300,6,270],
        #         [400,4,370],
        #         [500,6,470],
        #         [550,7,520],
        #         [600,9,570],
        #         [650,10,620],
        #         [700,4,670],
        #         [800,6,770],
        #         [900,4,870],
        #         ]

#         for misille in level:
# #            pro = Projectil(misille[0],misille[1])
#             lance = Lance_rocket(misille[2])
# #            self.pro_list.add(pro)
#             self.lance_list.add(lance)

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
