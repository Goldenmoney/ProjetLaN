import pygame
from pygame.locals import *
pygame.init()
from Classes.Level import *
from Classes.Player import *
from Classes.Lancerocket import *
from Classes.Projectile import *
import time
import sys #module systeme
from Classes.Piece import *
from threading import Timer

#============================= A GARDER =======================================#
"""Ajout des images menu"""
background = pygame.image.load("images/background.png").convert_alpha()
titre = pygame.image.load("images/titre.png").convert_alpha()
jouer0 = pygame.image.load("images/jouer.png").convert_alpha()
jouer = pygame.transform.scale(jouer0, (300, 100))
options0 = pygame.image.load("images/options.png").convert_alpha()
options = pygame.transform.scale(options0, (300, 100))
credits0 = pygame.image.load("images/credits.png").convert_alpha()
credits = pygame.transform.scale(credits0, (300, 100))
quitter0 = pygame.image.load("images/quitter.png").convert_alpha()
quitter = pygame.transform.scale(quitter0, (300, 100))

"""Ajout des images options"""
choixlvl = pygame.image.load("images/choixlvl.png").convert_alpha()
lvl_10 = pygame.image.load("images/1.png").convert_alpha()
lvl_1 = pygame.transform.scale(lvl_10, (300, 100))
lvl_20 = pygame.image.load("images/2.png").convert_alpha()
lvl_2 = pygame.transform.scale(lvl_20, (300, 100))
lvl_30 = pygame.image.load("images/3.png").convert_alpha()
lvl_3 = pygame.transform.scale(lvl_30, (300, 100))


#==============================================================================#

# menu gameover
Gameover_quit = pygame.image.load("img/exit.png").convert_alpha()
Gameover_quit_en = pygame.image.load("img/exiten.png").convert_alpha()
Gameover_menu = pygame.image.load("img/menu.png").convert_alpha()
Gameover_menu_en = pygame.image.load("img/menuen.png").convert_alpha()
Gameover_tryagain = pygame.image.load("img/tryagain.png").convert_alpha()
Gameover_tryagain_en = pygame.image.load("img/tryagainen.png").convert_alpha()

# menu victoire
credit = pygame.image.load("img/credit.png").convert_alpha()
credi_en = pygame.image.load("img/crediten.png").convert_alpha()
lvl_suivant = pygame.image.load("img/levelsuivant.png").convert_alpha()
lvl_suivant_en = pygame.image.load("img/levelsuivanten.png").convert_alpha()

# menu credit
Creditfinal = pygame.image.load("img/creditfinal.png").convert_alpha()


# fond
fond_menu = pygame.image.load("img/fondmenu.png").convert_alpha()
fond_base = pygame.image.load("img/fond.png").convert_alpha()
titreaenlever = pygame.image.load("img/titre.png").convert_alpha()
Victoire = pygame.image.load("img/youwin.png").convert_alpha()

"""musique"""
##musique_jeux = pygame.mixer.music.load('music/musiqueenjeux.mp3')
##musique_menu = pygame.mixer.music.load('music/musiquemenu.mp3')
##musique_mort = pygame.mixer.music.load('music/musiquemort.mp3')
##musique_victoire = pygame.mixer.music.load('music/musiquevictoire.mp3')

#============================= A GARDER =======================================#


# creation des variable de base
pygame.display.set_caption("CHICAGO ADVENTURE")

clock = pygame.time.Clock()
Display_Width = 1024
Display_Height = 768

Display = pygame.display.set_mode((Display_Width,Display_Height))

global level_en_cours_numero

FPS = 60

def Menu_Start(): ##A GARDER
    global level_en_cours_numero
    menuStart = True
    while menuStart:
        positionSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if pla.collidepoint(positionSouris):

                    #Display.blit(play_en,(320,185)) # Image quand bouton enfoncé
                    pygame.display.update()
                    time.sleep(1)

                    menu_niveau()

                if opt.collidepoint(positionSouris):

                    #Display.blit(Exit_en,(320,430))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

                if quit.collidepoint(positionSouris):

                    #Display.blit(option_en,(320,310))
                    pygame.display.update()
                    time.sleep(1)

                    GameLoop()

        Display.blit(background,(0,0))
        titr = Display.blit(titre,(0,0))
        pla = Display.blit(jouer,(362,335))
        opt = Display.blit(options,(362,460))
        quit =  Display.blit(quitter,(362,580))
        pygame.display.flip()


# affiche menu pour choix niveau
def menu_niveau():
    global level_en_cours_numero
    MenuOptions = True

    pygame.key.set_repeat(400,30)
    while MenuOptions:
        posSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if lvl1.collidepoint(posSouris):

                    #Display.blit(lvl_1_en,(370,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 1
                    #pygame.mixer.music.stop()
                    GameLoop()

                if lvl2.collidepoint(posSouris):

                    #Display.blit(lvl_2_en,(470,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 2
                    #pygame.mixer.music.stop()
                    GameLoop()


                if lvl3.collidepoint(posSouris):

                    #Display.blit(lvl_3_en,(570,250))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = 3
                    #pygame.mixer.music.stop()
                    GameLoop()

        Display.blit(background,(0,0))
        Display.blit(choixlvl,(0,0))
        lvl1 = Display.blit(lvl_1,(50,320))
        lvl2 = Display.blit(lvl_2,(370,320))
        lvl3 =  Display.blit(lvl_3,(690,320))
        pygame.display.flip()

#==============================================================================#


# def Menu_Base():
#     global level_en_cours_numero
#     MenuBase = True
#     pygame.mixer.music.stop()
#     pygame.mixer.music.load('music/musiquemenu.mp3')
#     pygame.mixer.music.play(-1)
#
#
#     pygame.key.set_repeat(400,30)
#
#     while MenuBase:
#         mpos = pygame.mouse.get_pos()
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#
#
#
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#
#                 if pla.collidepoint(mpos):
#
#                     Display.blit(play_en,(320,185))
#                     pygame.display.update()
#                     time.sleep(1)
#
#                     menu_niveau()
#
#                 if Exi.collidepoint(mpos):
#
#                     Display.blit(Exit_en,(320,430))
#                     pygame.display.update()
#                     time.sleep(1)
#                     pygame.quit()
#                     sys.exit()
#
#                 if Optio.collidepoint(mpos):
#
#                     Display.blit(option_en,(320,310))
#                     pygame.display.update()
#                     time.sleep(1)
#
#                     GameLoop()
#
#
#
#         Display.blit(fond_menu,(0,0))
#         pla = Display.blit(play,(320,185))
#         Exi = Display.blit(Exit,(320,430))
#         Optio =  Display.blit(option,(320,310))
#         pygame.display.flip()

# affiche menu quand on pert comme une merde
def Menu_gameover():
    global level_en_cours_numero
    MenuGameover = True
    pygame.mixer.music.stop()

    pygame.mixer.music.load('music/musiquemort.mp3')
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
                    Menu_Start()

        Display.blit(fond_base,(0,0))

        TryO = Display.blit(Gameover_tryagain,(340,200))
        ExiO = Display.blit(Gameover_quit,(650,300))
        MenuO =  Display.blit(Gameover_menu,(360,300))
        pygame.display.flip()

# affiche Credit
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
                    Menu_Start()


        Display.blit(fond_base,(0,0))
        Display.blit(Creditfinal,(0,0))

        MenuC =  Display.blit(Gameover_menu,(40,570))
        pygame.display.flip()

# affiche Menu_Victoire
def Menu_Victoire():
    global level_en_cours_numero
    MenuVictoire = True

    pygame.mixer.music.stop()
    pygame.mixer.music.load('music/musiquevictoire.mp3')
    pygame.mixer.music.play(-1)

    pygame.key.set_repeat(400,30)
    while MenuVictoire:
        posSouris = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if Suivant.collidepoint(posSouris):

                    Display.blit(lvl_suivant_en,(650,300))
                    pygame.display.update()
                    time.sleep(1)
                    level_en_cours_numero = level_en_cours_numero + 1
                    if level_en_cours_numero == 11:
                        level_en_cours_numero = 10
                    pygame.mixer.music.stop()
                    GameLoop()
                if CreditV.collidepoint(posSouris):

                    Display.blit(credi_en,(900,570))
                    pygame.display.update()
                    time.sleep(1)
                    Credit()


                if MenuV.collidepoint(posSouris):

                    Display.blit(Gameover_menu_en,(370,300))
                    pygame.display.update()
                    time.sleep(1)
                    pygame.mixer.music.stop()
                    Menu_Start()

        Display.blit(fond_base,(0,0))
        Display.blit(Victoire,(0,0))

        Suivant = Display.blit(lvl_suivant,(650,300))
        CreditV = Display.blit(credit,(900,570))
        MenuV =  Display.blit(Gameover_menu,(370,300))
        pygame.display.flip()


def GameLoop():
    global level_en_cours_numero

    GameRun = True
    GameOver = False
    i = 0
    posPersoX = 0
    posPersoY = 0
    player = Player()
    level_list = []
    # append ajouter element a la fin
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

    # grace a level_en_cours_numero(entier) on recupere la position dans la liste et donc le lvl dans la liste
    level_en_cours = level_list[level_en_cours_numero]

    player.level = level_en_cours
    sprite_bouge = pygame.sprite.Group()
    sprite_bouge.add(player)
    piece = Piece(Display)
    piece.randomize()
    piece.draw()

    while GameRun:
            print(i)
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
                        posPersoX = -3.5
                        posPersoY = 0

                    if event.key == K_RIGHT:
                        posPersoX = 3.5
                        posPersoY = 0

                    if event.key == K_SPACE:
                        posPersoX = 0
                        posPersoY = -3.5

            if event.type == KEYUP:
                    if event.key == K_LEFT:
                        posPersoX = 0
                        posPersoY = 0
                    if event.key == K_RIGHT:
                        posPersoX = 0
                        posPersoY = 0

            player.update(posPersoX,posPersoY)

            #collision_player_missile_mask =  pygame.sprite.spritecollide(player,level_en_cours.pro_list,False,pygame.sprite.collide_mask)
            #collision_player_missile = pygame.sprite.spritecollide(player,level_en_cours.pro_list,False)
            collision_player_fin = pygame.sprite.spritecollide(player,level_en_cours.portal,False)


            #if collision_player_missile:
            #    if collision_player_missile_mask:
            #        GameOver = True
            #        son_decolage.stop()




            if collision_player_fin:
                time.sleep(1)
                pygame.mixer.music.stop()
                Menu_Victoire()


            level_en_cours.update()
            level_en_cours.draw(Display)
            sprite_bouge.draw(Display)

            if i!=1200:
                piece.draw()

            if i == 1200:
                piece = Piece(Display)
                piece.randomize()
                piece.draw()
                i = 0

            pygame.display.update()
            i += 1

            # gere les FPS
            clock.tick(FPS)