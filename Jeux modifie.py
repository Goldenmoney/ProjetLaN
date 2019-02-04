import pygame
from pygame.locals import *
import sys #module systeme
pygame.init()
import time
import random

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
"""creation des variable de base"""
pygame.display.set_caption("GamedDev")

clock = pygame.time.Clock()
Display_Width = 1200
Display_Height = 675

"""musique"""
##musique_jeux = pygame.mixer.music.load('musiqueenjeux.mp3')
##musique_menu = pygame.mixer.music.load('musiquemenu.mp3')
##musique_mort = pygame.mixer.music.load('musiquemort.mp3')
##musique_victoire = pygame.mixer.music.load('musiquevictoire.mp3')

Display = pygame.display.set_mode((Display_Width,Display_Height))
fond =pygame.image.load("fond_jeux.png").convert()
fond = pygame.transform.scale(fond,(Display_Width,Display_Height))
FPS = 60
prolist =[]
pro = pygame.image.load("missile.png").convert_alpha()

pro = pygame.transform.scale(pro,(20,40))

rocket = pygame.image.load("Rocket.png").convert_alpha()

rocket = pygame.transform.scale(rocket,(80,80))

fond_menu = pygame.image.load("fondmenu.png").convert_alpha()
fond_base = pygame.image.load("fond.png").convert_alpha()
titre = pygame.image.load("titre.png").convert_alpha()
Victoire = pygame.image.load("youwin.png").convert_alpha()
portail_fin = pygame.image.load("portailfin.png").convert_alpha()
portail_fin = pygame.transform.scale(portail_fin,(128,128))

son_decolage = pygame.mixer.Sound("decolage.wav")

"""menu image base"""
play = pygame.image.load("boutonplay.png").convert_alpha()
play_en = pygame.image.load("boutonplayenfoncer.png").convert_alpha()
option =  pygame.image.load("boutonoption.png").convert_alpha()
option_en =  pygame.image.load("boutonoptionenfoncer.png").convert_alpha()
Exit =  pygame.image.load("boutonexit.png").convert_alpha()
Exit_en = pygame.image.load("boutonexitenfoncer.png").convert_alpha()

"""choix des niveau menu image"""
lvl_1 = pygame.image.load("1.png").convert_alpha()
lvl_1_en = pygame.image.load("1en.png").convert_alpha()
lvl_2 = pygame.image.load("2.png").convert_alpha()
lvl_2_en = pygame.image.load("2en.png").convert_alpha()
lvl_3 = pygame.image.load("3.png").convert_alpha()
lvl_3_en = pygame.image.load("3en.png").convert_alpha()
lvl_4 = pygame.image.load("4.png").convert_alpha()
lvl_4_en = pygame.image.load("4en.png").convert_alpha()
lvl_5 = pygame.image.load("5.png").convert_alpha()
lvl_5_en = pygame.image.load("5en.png").convert_alpha()
lvl_6 = pygame.image.load("6.png").convert_alpha()
lvl_6_en = pygame.image.load("6en.png").convert_alpha()
lvl_7 = pygame.image.load("7.png").convert_alpha()
lvl_7_en = pygame.image.load("7en.png").convert_alpha()
lvl_8 = pygame.image.load("8.png").convert_alpha()
lvl_8_en = pygame.image.load("8en.png").convert_alpha()
lvl_9 = pygame.image.load("9.png").convert_alpha()
lvl_9_en = pygame.image.load("9en.png").convert_alpha()
lvl_10 = pygame.image.load("10.png").convert_alpha()
lvl_10_en = pygame.image.load("10en.png").convert_alpha()
lvl_alea = pygame.image.load("aleatoire.png").convert_alpha()
lvl_alea_en = pygame.image.load("aleatoireen.png").convert_alpha()
Titre_Choix_lvl = pygame.image.load("choixduniveau.png").convert_alpha()

"""menu gameover"""
Gameover_quit = pygame.image.load("exit.png").convert_alpha()
Gameover_quit_en = pygame.image.load("exiten.png").convert_alpha()
Gameover_menu = pygame.image.load("menu.png").convert_alpha()
Gameover_menu_en = pygame.image.load("menuen.png").convert_alpha()
Gameover_tryagain = pygame.image.load("tryagain.png").convert_alpha()
Gameover_tryagain_en = pygame.image.load("tryagainen.png").convert_alpha()

"""menu victoire"""
credit = pygame.image.load("credit.png").convert_alpha()
credi_en = pygame.image.load("crediten.png").convert_alpha()
lvl_suivant = pygame.image.load("levelsuivant.png").convert_alpha()
lvl_suivant_en = pygame.image.load("levelsuivanten.png").convert_alpha()

"""menu credit"""
Creditfinal = pygame.image.load("creditfinal.png").convert_alpha()



"""image pour mouvement perso"""
move_image1 = pygame.image.load("move\segway1.png").convert_alpha()
move_image2 = pygame.image.load("move\segway2.png").convert_alpha()
move_image3 = pygame.image.load("move\segway3.png").convert_alpha()
move_image4 = pygame.image.load("move\segway4.png").convert_alpha()



move_image1 = pygame.transform.scale(move_image1,(64,128))
move_image2 = pygame.transform.scale(move_image2,(64,128))
move_image3 = pygame.transform.scale(move_image3,(64,128))
move_image4 = pygame.transform.scale(move_image4,(64,128))

global level_en_cours_numero


class Projectil(pygame.sprite.Sprite):
    def __init__(self,X,chute):
        pygame.sprite.Sprite.__init__(self)
        prolist = []
        Y =0
        self.X = X
        self.Y =Y
        self.chute = chute


        self.rect = pygame.Rect(X,Y,20,40)
        self.image = pro






    def Fall(self):
        self.Y += self.chute

        if self.Y >= Display_Height-10:
            self.Y = 0
            son_decolage.set_volume(0.1)
            son_decolage.play()
        self.rect = pygame.Rect(self.X,self.Y,20,40)
        self.mask = pygame.mask.from_surface(self.image)
        Display.blit(self.image,self.rect)


class Lance_rocket(pygame.sprite.Sprite):
    def __init__(self,X_pro):
        pygame.sprite.Sprite.__init__(self)
        self.X_pro = X_pro


        self.rect = rocket.get_rect()
        self.rect.x = self.X_pro
        self.rect.y = -10
        self.image = rocket


    def Update(self):
        Display.blit(self.image,(self.rect))



class Portailfin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = portail_fin.get_rect()
        self.rect.x = Display_Width-128
        self.rect.y = Display_Height-90-24-64
        self.image = portail_fin

class Player(pygame.sprite.Sprite):
    def __init__(self):
##        super().__init__()
        self.rect = move_image1.get_rect()
        self.rect.y = Display_Height-90-24-64
        self.rect.x = 0
        pygame.sprite.Sprite.__init__(self)
        self.animation_speed_init = 10
        self.animation_speed= self.animation_speed_init
        self.animation_list = [move_image1,move_image2,move_image3,move_image4]
        self.animation_position = 0
        self.animation_maximun = 3#len(self.animation)-1
        self.image = move_image1
        self.update(1)
        self.Gamelost = False

    def update(self,position):

        if position != 0:
            self.animation_speed -= 1
            self.rect.x += position
##            self.rect.y += position
            if self.animation_speed == 0:
                self.image = self.animation_list[self.animation_position]
                self.animation_speed = self.animation_speed_init
                if self.animation_position == self.animation_maximun:
                    self.animation_position = 0
                else:
                    self.animation_position += 1
        Display.blit(self.image,(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)



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



def message_to_screen(msg,color,X,Y):
    font = pygame.font.SysFont("monospace", 15)
    screen_text = font.render(msg, True, color)
    Display.blit(screen_text, [X,Y])

pygame.key.set_repeat(4,30)

def Menu_Base():
    global level_en_cours_numero
    MenuBase = True
    pygame.mixer.music.stop()
    pygame.mixer.music.load('musiquemenu.mp3')
    pygame.mixer.music.play(-1)


    pygame.key.set_repeat(400,30)

    while MenuBase:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()




            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if pla.collidepoint(mpos):

                    Display.blit(play_en,(320,185))
                    pygame.display.update()
                    time.sleep(1)

                    menu_level()

                if Exi.collidepoint(mpos):

                    Display.blit(Exit_en,(320,430))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

                if Optio.collidepoint(mpos):

                    Display.blit(option_en,(320,310))
                    pygame.display.update()
                    time.sleep(1)

                    GameLoop()



        Display.blit(fond_menu,(0,0))
        pla = Display.blit(play,(320,185))
        Exi = Display.blit(Exit,(320,430))
        Optio =  Display.blit(option,(320,310))
        pygame.display.flip()


def Menu_gameover():
    global level_en_cours_numero
    MenuGameover = True
    pygame.mixer.music.stop()

    pygame.mixer.music.load('musiquemort.mp3')
    pygame.mixer.music.play(-1)

    pygame.key.set_repeat(400,30)
    while MenuGameover:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()





            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if TryO.collidepoint(mpos):

                    Display.blit(Gameover_tryagain_en,(340,200))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.mixer.music.stop()
                    GameLoop()


                if ExiO.collidepoint(mpos):

                    Display.blit(Gameover_quit_en,(650,300))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

                if MenuO.collidepoint(mpos):

                    Display.blit(Gameover_menu_en,(360,300))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.mixer.music.stop()
                    Menu_Base()



        Display.blit(fond_base,(0,0))

        TryO = Display.blit(Gameover_tryagain,(340,200))
        ExiO = Display.blit(Gameover_quit,(650,300))
        MenuO =  Display.blit(Gameover_menu,(360,300))
        pygame.display.flip()

def menu_level():
    global level_en_cours_numero
    MenuLevel = True



    pygame.key.set_repeat(400,30)
    while MenuLevel:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()





            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if lvl1.collidepoint(mpos):

                    Display.blit(lvl_1_en,(370,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 0
                    pygame.mixer.music.stop()
                    GameLoop()

                if lvl2.collidepoint(mpos):

                    Display.blit(lvl_2_en,(470,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 1
                    pygame.mixer.music.stop()
                    GameLoop()


                if lvl3.collidepoint(mpos):

                    Display.blit(lvl_3_en,(570,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 2
                    pygame.mixer.music.stop()
                    GameLoop()

                if lvl4.collidepoint(mpos):

                    Display.blit(lvl_4_en,(670,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 3
                    pygame.mixer.music.stop()
                    GameLoop()

                if lvl5.collidepoint(mpos):

                    Display.blit(lvl_5_en,(770,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 4
                    pygame.mixer.music.stop()
                    GameLoop()

                if lvl6.collidepoint(mpos):

                    Display.blit(lvl_6_en,(370,350))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 5
                    pygame.mixer.music.stop()
                    GameLoop()


                if lvl7.collidepoint(mpos):

                    Display.blit(lvl_7_en,(470,350))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 6
                    pygame.mixer.music.stop()
                    GameLoop()

                if lvl8.collidepoint(mpos):

                    Display.blit(lvl_8_en,(570,350))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero =7
                    pygame.mixer.music.stop()
                    GameLoop()

                if lvl9.collidepoint(mpos):

                    Display.blit(lvl_9_en,(670,350))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 8
                    pygame.mixer.music.stop()
                    GameLoop()


                if lvl10.collidepoint(mpos):
                    Display.blit(lvl_10_en,(770,350))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 9
                    pygame.mixer.music.stop()
                    GameLoop()


                if lvlalea.collidepoint(mpos):
                    Display.blit(lvl_alea_en,(470,450))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 10
                    pygame.mixer.music.stop()
                    GameLoop()



        Display.blit(fond_base,(0,0))
        Display.blit(Titre_Choix_lvl,(0,0))
        lvl1 = Display.blit(lvl_1,(370,250))
        lvl2 = Display.blit(lvl_2,(470,250))
        lvl3 =  Display.blit(lvl_3,(570,250))
        lvl4 =  Display.blit(lvl_4,(670,250))
        lvl5 =  Display.blit(lvl_5,(770,250))
        lvl6 =  Display.blit(lvl_6,(370,350))
        lvl7 =  Display.blit(lvl_7,(470,350))
        lvl8 =  Display.blit(lvl_8,(570,350))
        lvl9 =  Display.blit(lvl_9,(670,350))
        lvl10 =  Display.blit(lvl_10,(770,350))
        lvlalea =  Display.blit(lvl_alea,(470,450))
        pygame.display.flip()

def Menu_Victoire():
    global level_en_cours_numero
    MenuVictoire = True

    pygame.mixer.music.stop()
    pygame.mixer.music.load('musiquevictoire.mp3')
    pygame.mixer.music.play(-1)

    pygame.key.set_repeat(400,30)
    while MenuVictoire:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()





            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if Suivant.collidepoint(mpos):

                    Display.blit(lvl_suivant_en,(650,300))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = level_en_cours_numero + 1
                    if level_en_cours_numero == 11:
                        level_en_cours_numero = 10
                    pygame.mixer.music.stop()
                    GameLoop()
                if CreditV.collidepoint(mpos):

                    Display.blit(credi_en,(900,570))
                    pygame.display.update()
                    time.sleep(1)
                    Credit()


                if MenuV.collidepoint(mpos):

                    Display.blit(Gameover_menu_en,(370,300))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.mixer.music.stop()
                    Menu_Base()



        Display.blit(fond_base,(0,0))
        Display.blit(Victoire,(0,0))

        Suivant = Display.blit(lvl_suivant,(650,300))
        CreditV = Display.blit(credit,(900,570))
        MenuV =  Display.blit(Gameover_menu,(370,300))
        pygame.display.flip()

def Credit():
    global level_en_cours_numero
    Menucredit = True



    pygame.key.set_repeat(400,30)
    while Menucredit:
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()





            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if MenuC.collidepoint(mpos):

                    Display.blit(Gameover_menu_en,(40,570))
                    pygame.display.update()
                    time.sleep(1)
                    Menu_Base()


        Display.blit(fond_base,(0,0))
        Display.blit(Creditfinal,(0,0))

        MenuC =  Display.blit(Gameover_menu,(40,570))
        pygame.display.flip()



def GameLoop():
    global level_en_cours_numero


    GameRun = True
    GameOver = False

    pos = 0
    player = Player()
    level_list = [ ]
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
    pygame.mixer.music.load('musiqueenjeux.mp3')
    pygame.mixer.music.play(-1)


    level_en_cours = level_list[level_en_cours_numero]

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


Menu_Base()















