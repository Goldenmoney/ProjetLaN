import pygame
pygame.init()
from Classes.Menu import *
from Classes.PortailFin import *
from Classes.Player import *
from Classes.Lancerocket import *
from Classes.Projectile import *
import random

global level_en_cours_numero

pro = pygame.image.load("img/missile.png").convert_alpha()

pro = pygame.transform.scale(pro,(20,40))

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

##        screen.fill()
        Display.blit(fond,(0,0))

        self.pro_list.draw(screen)
        self.lance_list.draw(screen)
        self.portal.draw(screen)





class Level_1(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[100,3,70],
                [200,6,170],
                [300,4,270],
                [400,6,370],
                [500,4,470],
                [600,6,570],
                [700,7,670],
                [800,3,770],
                [900,5,870],
                [1000,4,970],
                [1100,6,1070],]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)


class Level_2(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[100,5,70],
                [200,10,170],
                [300,7,270],
                [400,8,370],
                [500,9,470],
                [600,4,570],
                [700,3,670],
                [800,9,770],
                [900,9,870],
                [1000,9,970],
                [1100,9,1070],]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_3(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[80,3,80-30],
                [150,2,120],
                [250,6,220],
                [300,6,270],
                [400,4,370],
                [500,6,470],
                [550,7,520],
                [600,9,570],
                [650,10,620],
                [700,4,670],
                [800,6,770],
                [900,4,870],
                ]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)


class Level_4(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[80,9,80-30],
                [150,10,120],
                [250,8,220],
                [300,7,270],
                [400,5,370],
                [500,8,470],
                [550,9,520],]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_5(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[80,3,80-30],
                [150,10,120],
                [250,4,220],
                [300,6,270],
                [400,4,370],
                [500,6,470],
                [550,7,520],
                [630,20,600],
                [800,5,770],
                [900,4,870],
                [950,4,930],
                [1000,4,970],
                [1050,4,1030],
                [1100,4,1070],]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_6(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[50,3,20],
                [100,10,70],
                [200,4,170],
                [300,6,270],
                [400,4,370],
                [500,6,470],
                [550,7,520],
                [600,3,570],
                [700,15,670],
                [800,5,770],
                [850,6,820],
                [900,7,870],
                [1000,6,970],
                [1000,7,970],]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_7(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[100,3,80-30],
                [100,6,120],
                [200,4,220],
                [300,5,270],
                [400,6,370],
                [500,7,470],
                [600,8,520],
                [700,9,80-30],
                [800,10,120],
                [900,11,220],
                [900,5,270],
                ]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_8(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[80,3,50],
                [80,4,50],
                [80,5,50],
                [80,6,50],
                [300,4,270],
                [300,5,270],
                [300,6,270],
                [300,7,270],
                [400,10,370],
                [500,4,470],
                [600,6,570],
                [700,4,670],
                [800,6,770],
                [900,7,870],]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_9(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[600,3,570],
                [600,10,570],
                [600,4,570],
                [600,6,570],
                [600,9,570],
                [600,5,570],
]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_10(Level):
    def __init__(self, player):


        Level.__init__(self, player)

        level =[[80,10,50],
                [80,5,50],
                [80,9,50],
                [80,7,50],
                [150,8,120],
                [150,6,120],
                [200,7,170],
                [250,7,220],
                [280,9,250],
                [300,12,370],
                [350,12,320],
                [450,15,420],
                [530,8,500],
                [570,7,540],
                [600,8,570],
                [650,9,620],
                [650,6,620],
                [650,8,620],
                [700,8,670],
                [700,9,670],
                [800,10,770],
                [900,13,870],
                [1000,10,970],
                [1000,9,970],
                [1000,5,970],
                [1000,13,970],
]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

class Level_alea(Level):
    def __init__(self, player):


        Level.__init__(self, player)
        a = random.randint(0,1200)
        b = random.randint(0,1200)
        c = random.randint(0,1200)
        d = random.randint(0,1200)
        e = random.randint(0,1200)
        f = random.randint(0,1200)
        g = random.randint(0,1200)
        h = random.randint(0,1200)
        i = random.randint(0,1200)
        j = random.randint(0,1200)
        rand_list = [a,b,c,d,e,f,g,h,i,j]
##        for i in rand_list:
##            if i == rand_list[-10:]+30 or i == rand_list[-10:]-30:
##                i = random.randrange(0,1200)a

        ac=random.randrange(2,12)
        bc=random.randrange(2,12)
        cc=random.randrange(2,12)
        dc=random.randrange(2,12)
        ec=random.randrange(2,12)
        fc=random.randrange(2,12)
        gc=random.randrange(2,12)
        hc=random.randrange(2,12)
        ic=random.randrange(2,12)
        jc=random.randrange(2,12)


        level =[[a,ac,a-30],
                [b,bc,b-30],
                [c,cc,c-30],
                [d,dc,d-30],
                [e,ec,e-30],
                [f,fc,f-30],
                [g,gc,g-30],
                [h,hc,h-30],
                [i,ic,i-30],
                [j,jc,j-30],

                            ]

        for misille in level:
            pro = Projectil(misille[0],misille[1])
            lance = Lance_rocket(misille[2])
            self.pro_list.add(pro)
            self.lance_list.add(lance)

def GameLoop():
    global level_en_cours_numero


    GameRun = True
    GameOver = False

    pos = 0
    player = Player()
    level_list = []
    level_list.append(Level_1(player))
    level_list.append(Level_2(player))
    level_list.append(Level_3(player))
    level_list.append(Level_4(player))
    level_list.append(Level_5(player))
    level_list.append(Level_6(player))
    level_list.append(Level_7(player))
    level_list.append(Level_8(player))
    level_list.append(Level_9(player))
    level_list.append(Level_10(player))
    level_list.append(Level_alea(player))

    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiqueenjeux.mp3')
    pygame.mixer.music.play(-1)

    global  levelchiffre
    levelchiffre=levelnum()
    level_en_cours = level_list[levelchiffre]

    player.level = level_en_cours
    sprite_bouge = pygame.sprite.Group()
    sprite_bouge.add(player)

    while GameRun:
            while GameOver == True:
                time.sleep(1)
                pygame.mixer.music.stop()
                Menu_gameover()


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        pos = -3.5


                    if event.key == K_RIGHT:
                        pos = 3.5
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        pos = 0
                    if event.key == K_RIGHT:
                        pos = 0


            player.update(pos)


            collision_player_missile_mask =  pygame.sprite.spritecollide(player,level_en_cours.pro_list,False,pygame.sprite.collide_mask)
            collision_player_missile = pygame.sprite.spritecollide(player,level_en_cours.pro_list,False)
            collision_player_fin = pygame.sprite.spritecollide(player,level_en_cours.portal,False)


            if collision_player_missile:
                if collision_player_missile_mask:
                    GameOver = True
                    son_decolage.stop()

            if collision_player_fin:
                time.sleep(1)
                pygame.mixer.music.stop()
                Menu_Victoire()

            level_en_cours.update()
            level_en_cours.draw(Display)
            sprite_bouge.draw(Display)


            pygame.display.update()



            clock.tick(FPS)
